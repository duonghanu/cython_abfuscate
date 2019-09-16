import numpy as np
from optimizer.class_medical_optimizer import Medical_optimizer

def run():
    ICDP_type = "ICDP_benefit"#"ICDP"#
    calibration_mode = "per_ICDP_model"#"universal_model"#
    cost_type = 'exponential_cost_lin_copay'#'exponential_cost_lin_segment'#

    computation = True

    if computation:
        instance = Medical_optimizer(claims_df=None, ICDP_type = ICDP_type,
                                 cost_type = cost_type, call_regularizer = 1e-2,
                                  calibration_mode = calibration_mode
                                  )
        instance.agnostic_calibrator()

        for ICDP, params in instance.parameters_ICDP.items():
            print("ICDP = ", ICDP)
            print("Size = ", np.sum(instance.member_mass_ICDP[ICDP]))
            print("Parameters = ", params)

    instance = Medical_optimizer(instance)
    discounts = instance.discounts_ICDP
    discounts_vector = instance.get_big_vector(discounts, df = "providers", method = 'erase')
    zero_discounts = dict()#instance.get_sub_vector()
    for ICDP in instance.ICDPs:
        zero_discounts[ICDP] = 0*discounts[ICDP]
    control_argument = instance.get_initial_control_argument()
    phi_probability = instance.compute_phi_proba(control_argument)
    #instance.compute_average_cost_ICDP()
    initial_dollar_price = instance.dollar_price(control_argument, discounts = zero_discounts)#['value']
    actual_price = instance.realized_price()
    non_segmented_price = instance.dollar_price(0*control_argument)#['value']
    print("Dollar_price = ", initial_dollar_price['value'])
    print("Dollar_price_members = ", initial_dollar_price['members_value'].sum())
    print("Dollar_price_providers = ", initial_dollar_price['providers_value'].sum())
    print("Actual_price = ", actual_price)
    print("No_seg_price = ", non_segmented_price['value'])

    #result_optimization = instance.optimize_network(test_gradient_contraint = False, test_gradient = False,
    #                                                method = 'SLSQP',#'trust-constr',#
    #                                                normalize_dollar_price = initial_dollar_price,
    #                                                phi_loss_tolerated = 100., phi_weaken = 0.)

    #optimal_price = instance.dollar_price(result_optimization['x'])['value']
    #print("Optim_price = ", optimal_price)
    #print("Optimality_ratio = ", (non_segmented_price - initial_dollar_price)/(non_segmented_price - optimal_price))
