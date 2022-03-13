# ==============================================================================
# description     :Optimization models
# author          :Roberto Pinto
# date            :2022.03.22
# version         :1.0
# notes           :This software is meant for teaching purpose only and it is provided as-is.
#                  The models and data are inspired by the book Watson, M., Lewis, S., Cacioppi, P., Jayaraman, J. (2013)
#                  Supply Chain Network Design, Pearson. All the data has been taken from the book
#                  The software is provided as-is, with no guarantee by the author
# ==============================================================================

import pulp as pl
import pandas as pd
import matplotlib.pyplot as plt
import pprint

dpi = 136
fig_x = 8
fig_y = 5

def print_dict(data):
    """ PrettyPrint the data """
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)


def optimal_location(num_warehouses=1,
                     warehouses=None,
                     customers=None,
                     distance=None,
                     distance_ranges=None,
                     forced_open=None,
                     forced_closed=None,
                     plot=False):
    """ Defines the optimal location of <num_warehouses> warehouses choosing from a set <warehouses> (p-median problem) """


    # check input
    if not warehouses or not customers  or not distance:
        print('At least one required parameter is missing')
        print('REQUIRED PARAMETERS: warehouses, customers, distance')
        return None
    if not distance_ranges:
        distance_ranges = [0]

    if distance_ranges[0] != 0:
        distance_ranges.insert(0, 0)

    if distance_ranges[-1] != 99999:
        distance_ranges.append(99999)


    # check if values in distance_ranges are increasing
    if not all([True if y-x > 0 else False for (x, y) in zip(distance_ranges, distance_ranges[1:])]):
        print('ERROR: distance_ranges parameters must contains values in strictly ascending order')
        return None

    # define the problem container
    pb = pl.LpProblem("Distance based model", pl.LpMinimize)
    
    warehouses_id = set(warehouses.keys())
    customers_id = set(customers.keys())
    # define variables

    # Customers assignment to warehouses
    assignment_vars = pl.LpVariable.dicts(name="Flow",
                                          indices=[(w, c) for w in warehouses_id for c in customers_id],
                                          lowBound=0,
                                          upBound=1,
                                          cat=pl.LpInteger)
    # Open warehouses
    facility_status_vars = pl.LpVariable.dicts(name="Open",
                                               indices=[w for w in warehouses_id],
                                               lowBound=0,
                                               upBound=1,
                                               cat=pl.LpInteger)
    
    # define the objective function (sum of all production costs)
    total_weighted_distance = pl.lpSum([customers[c].demand * distance[w, c] * assignment_vars[w, c] 
                                        for w in warehouses_id for c in customers_id]) / pl.lpSum([customers[c].demand for c in customers_id])
    
    # setting problem objective
    pb.setObjective(total_weighted_distance)  
    
    # set constraints
    for c in customers_id:
        pb += pl.LpConstraint(e = pl.lpSum([assignment_vars[w, c] for w in warehouses_id]), 
                              sense=pl.LpConstraintEQ, 
                              name=f"Customer_{c}_Served", 
                              rhs=1)

    pb += pl.LpConstraint(e = pl.lpSum([facility_status_vars[w] for w in warehouses_id]),
                          sense=pl.LpConstraintEQ,
                          rhs=num_warehouses,
                          name=f"Num_of_active_warehouses")
    
    for w in warehouses_id:
        for c in customers_id:
            pb += pl.LpConstraint(e = assignment_vars[w, c] - facility_status_vars[w],
                                  sense=pl.LpConstraintLE,
                                  rhs=0,
                                  name=f"Logical_constraint_between_customer_{c}_and_warehouse_{w}")
    
    # Force open warehouses
    if forced_open and isinstance(forced_open, list):
        print(f'Forcing open warehouses: {forced_open}')
        for w in forced_open:
            try:
                facility_status_vars[w].lowBound = 1
            except KeyError:
                print(f'Warehouse {w} does not exist')

    # Force closed warehouses
    if forced_closed and isinstance(forced_closed, list):
        print(f'Forcing closed warehouses: {forced_closed}')
        for w in forced_closed:
            try:
                facility_status_vars[w].upBound = 0
            except KeyError:
                print(f'Warehouse {w} does not exist')


    # The problem is solved using PuLP's choice of Solver
    _solver = pl.PULP_CBC_CMD(keepFiles=False,
                              gapRel=0.00,
                              timeLimit=120, 
                              msg=True)
    pb.solve(solver=_solver)
    
    print("Optimization Status ", pl.LpStatus[pb.status] ) #print in Jupyter Notebook
    if pl.LpStatus[pb.status] == "Infeasible" :
        print("********* ERROR: Model not feasible, don't use results.")

    # print objective
    flows = {(w, c) for w in warehouses_id for c in customers_id if assignment_vars[w, c].varValue > 0}
    
    active_warehouses = {w for w in warehouses_id if facility_status_vars[w].varValue == 1}
    avg_weighted_distance = pl.value(pb.objective)
    print(f'Average weighted distance: {round(avg_weighted_distance, 0)}')
    print()
    print(f'Open warehouses:')
    total_outflow = 0.
    for w in active_warehouses:
        try:
            outflow = sum([customers[c].demand * assignment_vars[w, c].varValue for c in customers_id])
        except TypeError:
            outflow = 0

        total_outflow += outflow            
        
        try:
            assigned_customers = int(sum([assignment_vars[w, c].varValue for c in customers_id if assignment_vars[w, c].varValue == 1]))
        except TypeError:
            assigned_customers = 0

        print(f'ID: {w:3} City: {warehouses[w][1]:20} State: {warehouses[w][2]:6} Num. customers: {assigned_customers:3}  Outflow: {outflow:11} units')
    print()
    print(f'Total outflow: {total_outflow} units')
    
    customers_assignment = []
    for (w, c) in assignment_vars.keys():
        if assignment_vars[(w, c)].varValue > 0:
            cust = {
                'Warehouse':str(warehouses[w].city) + ', ' + str(warehouses[w].state),
                'Customer':str(customers[c].city) + ', ' + str(customers[c].state),
                'Customer Demand': customers[c].demand,
                'Distance': distance[w,c],
                'Warehouse Latitude' : warehouses[w].latitude,
                'Warehouse Longitude' : warehouses[w].longitude,
                'Customers Latitude' : customers[c].latitude,
                'Customers Longitude': customers[c].longitude
            }
            customers_assignment.append(cust)
                  
    df_cu = pd.DataFrame.from_records(customers_assignment)
    df_cu = df_cu[['Warehouse', 'Customer', 'Distance', 'Customer Demand']]    
    labels = list(range(1, len(distance_ranges)))
    df_cu['distance_range'] = pd.cut(df_cu['Distance'], 
                                     bins=distance_ranges,
                                     labels=labels,
                                     include_lowest=True)
    
    total_demand = sum(df_cu['Customer Demand'])
    demand_perc_by_ranges = {}
    for band in labels:
        perc_of_demand_in_band = sum(df_cu[df_cu['distance_range']== band]['Customer Demand']) / total_demand
        distance_range_lower_limit = distance_ranges[band-1]
        distance_range_upper_limit = distance_ranges[band]
        print(f'% of demand in range {distance_range_lower_limit:5} - {distance_range_upper_limit:5}: {round(perc_of_demand_in_band * 100, 0):>3}')
        demand_perc_by_ranges[(distance_range_lower_limit, distance_range_upper_limit)] = perc_of_demand_in_band

    print(f"Most distant customer is at {df_cu['Distance'].max()}")

    if plot:
        plt.figure(figsize=(fig_x, fig_y), dpi=dpi)

        # Plot flows
        for flow in flows:
            plt.plot(
                    [warehouses[flow[0]].longitude, customers[flow[1]].longitude],
                    [warehouses[flow[0]].latitude, customers[flow[1]].latitude],
                    color="k",
                    linestyle="-",
                    linewidth=0.3)
        
        # Plot customers
        for _, each in customers.items():
            plt.plot(each.longitude, each.latitude, "*b", markersize=4)
        
        # Plot active warehouses
        for k, each in warehouses.items():
            if k in active_warehouses:
                plt.plot(each.longitude, each.latitude, "sr", markersize=4)

        # Remove axes
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)

    return {'objective_value': pl.value(pb.objective),
            'avg_weighted_distance': avg_weighted_distance,
            'active_warehouses_id': active_warehouses,
            'active_warehouses_name': [warehouses[w].name for w in active_warehouses],
            'most_distant_customer': df_cu['Distance'].max(),
            'demand_perc_by_ranges': demand_perc_by_ranges
            }


def optimal_location_service_level(num_warehouses=3,
                                   warehouses=None,
                                   customers=None,
                                   distance=None,
                                   distance_ranges=None,
                                   high_service_distance=800,
                                   avg_service_distance=None,
                                   max_service_distance=None,
                                   forced_open=None,
                                   forced_closed=None,
                                   plot=True):
    """ Defines the optimal location of <num_warehouses> warehouses choosing from a set <warehouses>
        maximising the demand covered within <high_service_distance> 
        high_service_distance: distance range within which the demand covered must be maximized
        avg_service_distance: largest average weighted distance tolerated
        max_service_distance: all customers must have a warehouse within this distance"""


    # check input
    if not warehouses or not customers or not distance:
        print('At least one required parameter is missing')
        print('REQUIRED PARAMETERS: warehouses, customers, distance')
        return None
    if not distance_ranges:
        distance_ranges = [0]

    if distance_ranges[0] != 0:
        distance_ranges.insert(0, 0)

    if distance_ranges[-1] != 99999:
        distance_ranges.append(99999)

    if not max_service_distance:
        max_service_distance = 99999


    # check if values in distance_ranges are increasing
    if not all([True if y-x > 0 else False for (x, y) in zip(distance_ranges, distance_ranges[1:])]):
        print('ERROR: distance_ranges parameters must contains values in strictly ascending order')
        return None

    # define the problem container
    pb = pl.LpProblem("ServiceLevelModel", pl.LpMaximize)
    
    warehouses_id = set(warehouses.keys())
    customers_id = set(customers.keys())

    # define variables

    # Customers assignment to warehouses
    assignment_vars = pl.LpVariable.dicts(name="Flow",
                                          indices=[(w, c) for w in warehouses_id for c in customers_id],
                                          lowBound=0,
                                          upBound=1,
                                          cat=pl.LpInteger)
    # Open warehouses
    facility_status_vars = pl.LpVariable.dicts(name="Open",
                                               indices=[w for w in warehouses_id],
                                               lowBound=0,
                                               upBound=1,
                                               cat=pl.LpInteger)
    
    # Setting the value to 1 if customer c is within the given high service distance of warehouse w
    high_service_dist_par = {(w, c): 1 if distance[w, c] <= high_service_distance else 0 for w in warehouses_id for c in customers_id}

    # Setting the value to 1 if customer c is within the given max service distance of warehouse w
    max_service_dist_par = {(w, c): 1 if distance[w, c] <= max_service_distance else 0 for w in warehouses_id for c in customers_id}

    # define the objective function (sum of all covered demand within <high_service_dist_par> distance)
    total_covered_demand_high_service = pl.lpSum([customers[c].demand * high_service_dist_par[w, c] * assignment_vars[w, c] 
                                                  for w in warehouses_id for c in customers_id]) / pl.lpSum([customers[c].demand for c in customers_id])
    
    # setting problem objective
    pb.setObjective(total_covered_demand_high_service)  
    
    # set constraints
    for c in customers_id:
        pb += pl.LpConstraint(e = pl.lpSum([assignment_vars[w, c] for w in warehouses_id]), 
                              sense=pl.LpConstraintEQ, 
                              name=f"Customer_{c}_Served", 
                              rhs=1)

    pb += pl.LpConstraint(e = pl.lpSum([facility_status_vars[w] for w in warehouses_id]),
                          sense=pl.LpConstraintEQ,
                          rhs=num_warehouses,
                          name=f"Num_of_active_warehouses")
    
    for w in warehouses_id:
        for c in customers_id:
            pb += pl.LpConstraint(e = assignment_vars[w, c] - facility_status_vars[w],
                                  sense=pl.LpConstraintLE,
                                  rhs=0,
                                  name=f"Logical_constraint_between_customer_{c}_and_warehouse_{w}")
    
    # Limit the average service distance to avoid random allocation of customer beyond the <high_service_distance> range
    if avg_service_distance:
        pb += pl.LpConstraint(e=pl.lpSum([distance[w, c] * customers[c].demand * assignment_vars[w, c] for w in warehouses_id for c in customers_id]) / pl.lpSum([customers[c].demand for c in customers_id]),
                              sense=pl.LpConstraintLE,
                              rhs=avg_service_distance,
                              name='Avoid_random_allocations' )

    # Forbid assignment to warehouses farther than <max_service_distance>. This may lead to infeasibility
    for w in warehouses_id:
        for c in customers_id:
            assignment_vars[w, c].upBound = max_service_dist_par[w, c]

    # Force open warehouses
    if forced_open and isinstance(forced_open, list):
        print(f'Forcing open warehouses: {forced_open}')
        for w in forced_open:
            try:
                facility_status_vars[w].lowBound = 1
            except KeyError:
                print(f'Warehouse {w} does not exist')

    # Force closed warehouses
    if forced_closed and isinstance(forced_closed, list):
        print(f'Forcing closed warehouses: {forced_closed}')
        for w in forced_closed:
            try:
                facility_status_vars[w].upBound = 0
            except KeyError:
                print(f'Warehouse {w} does not exist')


    # The problem is solved using PuLP's choice of Solver
    _solver = pl.PULP_CBC_CMD(keepFiles=False,
                              gapRel=0.00,
                              timeLimit=120, 
                              msg=True)
    pb.solve(solver=_solver)
    
    print("Optimization Status ", pl.LpStatus[pb.status] ) #print in Jupyter Notebook
    if pl.LpStatus[pb.status] == "Infeasible" :
        print("********* ERROR: Model not feasible, don't use results.")

    # print objective
    flows = {(w, c) for w in warehouses_id for c in customers_id if assignment_vars[w, c].varValue > 0}
    
    active_warehouses = {w for w in warehouses_id if facility_status_vars[w].varValue == 1}
    
    perc_covered_demand_high_service = pl.value(pb.objective)
    print(f'% covered demand within {high_service_distance} distance: {round(perc_covered_demand_high_service * 100, 1)}%')
    print()
    print(f'Open warehouses:')
    total_outflow = 0.
    for w in active_warehouses:
        try:
            outflow = sum([customers[c].demand * assignment_vars[w, c].varValue for c in customers_id])
        except TypeError:
            outflow = 0

        total_outflow += outflow            
        
        try:
            assigned_customers = int(sum([assignment_vars[w, c].varValue for c in customers_id if assignment_vars[w, c].varValue == 1]))
        except TypeError:
            assigned_customers = 0

        print(f'ID: {w:3} City: {warehouses[w][1]:20} State: {warehouses[w][2]:6} Num. customers: {assigned_customers:3}  Outflow: {outflow:11} units')
    print()
    print(f'Total outflow: {total_outflow} units')
    
    customers_assignment = []
    for (w, c) in assignment_vars.keys():
        if assignment_vars[(w, c)].varValue > 0:
            cust = {
                'Warehouse':str(warehouses[w].city) + ', ' + str(warehouses[w].state),
                'Customer':str(customers[c].city) + ', ' + str(customers[c].state),
                'Customer Demand': customers[c].demand,
                'Distance': distance[w,c],
                'Warehouse Latitude' : warehouses[w].latitude,
                'Warehouse Longitude' : warehouses[w].longitude,
                'Customers Latitude' : customers[c].latitude,
                'Customers Longitude': customers[c].longitude
            }
            customers_assignment.append(cust)
                  
    df_cu = pd.DataFrame.from_records(customers_assignment)
    df_cu = df_cu[['Warehouse', 'Customer', 'Distance', 'Customer Demand']]    
    labels = list(range(1, len(distance_ranges)))
    df_cu['distance_range'] = pd.cut(df_cu['Distance'], 
                                     bins=distance_ranges,
                                     labels=labels,
                                     include_lowest=True)
    
    total_demand = sum(df_cu['Customer Demand'])
    demand_perc_by_ranges = {}
    for band in labels:
        perc_of_demand_in_band = sum(df_cu[df_cu['distance_range'] == band]['Customer Demand']) / total_demand
        distance_range_lower_limit = distance_ranges[band-1]
        distance_range_upper_limit = distance_ranges[band]
        print(f'% of demand in range {distance_range_lower_limit:5} - {distance_range_upper_limit:5}: {round(perc_of_demand_in_band * 100, 0):>3}')
        demand_perc_by_ranges[(distance_range_lower_limit, distance_range_upper_limit)] = perc_of_demand_in_band

    print(f"Most distant customer is at {df_cu['Distance'].max()}")

    df_cu['Weighted_Distance'] = df_cu['Distance'] * df_cu['Customer Demand']
    avg_weighted_distance = df_cu['Weighted_Distance'].sum() / df_cu['Customer Demand'].sum()

    if plot:
        plt.figure(figsize=(fig_x, fig_y), dpi=dpi)

        # Plot flows
        for flow in flows:
            plt.plot(
                    [warehouses[flow[0]].longitude, customers[flow[1]].longitude],
                    [warehouses[flow[0]].latitude, customers[flow[1]].latitude],
                    color="k",
                    linestyle="-",
                    linewidth=0.3)
        
        # Plot customers
        for _, each in customers.items():
            plt.plot(each.longitude, each.latitude, "*b", markersize=4)
        
        # Plot active warehouses
        for k, each in warehouses.items():
            if k in active_warehouses:
                plt.plot(each.longitude, each.latitude, "sr", markersize=4)

        # Remove axes
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.gca().axes.get_yaxis().set_visible(False)

    return {'objective_value': pl.value(pb.objective),
            'avg_weighted_distance': avg_weighted_distance,
            'active_warehouses_id': active_warehouses,
            'active_warehouses_name': [warehouses[w].name for w in active_warehouses],
            'most_distant_customer': df_cu['Distance'].max(),
            'demand_perc_by_ranges': demand_perc_by_ranges
            }                                   