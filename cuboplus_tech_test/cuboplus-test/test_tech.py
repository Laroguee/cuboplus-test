# constants

max_supply_btc=21000000 #max btc supply
btc_to_sats=100000000 # btc equal to sats
blocks_each_halving=210000 # halving every 210,000 blocks
initial_Reward_btc=50 #initial btc reward
maxHalvings=33 # the reward will approach zero

def calculateSupply():
    total_btc_mined=0 #total mined btc
    blockReward=initial_Reward_btc #initial reward in btc
    halving=0 #count of halving

    for halving in range(1,maxHalvings+1):
        #calculate the block reward in sats
        rewardSats=blockReward*btc_to_sats
        blocksMined=blocks_each_halving
        btc_mined_halving=blockReward*blocksMined
        total_btc_mined+=btc_mined_halving

        #convertion to sats
        totalSatsMined=total_btc_mined*btc_to_sats
        percentMined=(total_btc_mined/max_supply_btc)*100

        #printing results

        print(f"halvings {halving}")
        print(f"block reward: {rewardSats:.0f} sats")
        print(f"total bitcoin supply: {totalSatsMined:.0f} sats")
        print(f"percentage mined: {percentMined:.2f}%\n")

        #halve block reward for next iteration
        blockReward/=2

        #stop if reward is zero
        if blockReward<1e-8:
            break

calculateSupply()