bumps_diff = 40  # The point difference required for a bump
nbump_extra = (2/3 * bumps_diff) * 5
max_nbump = 3
nbump_diff = [round((i*nbump_extra + bumps_diff), 2)
              for i in range(max_nbump+1)]

zero_point_msgs = ["did not turn up", "had a Faulty Coxbox",
                   "boated without a lifejacket", "had no bowball", "caught a crab off the start"]
