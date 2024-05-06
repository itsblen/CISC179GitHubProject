# CISC179GitHubProject
 MapleLegends scrolling simulator script

Abstract: This program is written to simulate millions of scrolling attempts on an item in MapleStory in order to estimate production cost.

Background
In the video game MapleStory, equipment that the player uses have a limited number of "Upgrades" available when they are initially generated.
Each of these Upgrades essentially gives the player an opportunity to use a "Scroll" in order to increase the potency of the item by increasing its Stat properties.
Each Scroll has a % chance to successfully be used or fail as well as certain Stats that it can upgrade, and by varying amounts, and some Scrolls have a chance to completely destroy the item when they fail.
Whenever a Scroll is used on an item, it will use up an Upgrade slot, regardless of whether the Scroll passes or fails.
Every item and Scroll can be traded, bought, or sold to/from other players, but due to the nature of passing/failing Scrolls, estimating the cost of items can sometimes be difficult.
This is especially notorious in the case of 'unfinished' items that still have Upgrade slots remaining, in which case players will frequently argue over the expected production cost of creating the item, and therefore the price it would expect to command.

This program will simulate an optimized Scrolling practice on a given item, with parameters for the following:
weapon_npc : the price that the base item can be sold to npc shops for in Mesos (the primary currency of the game)
weapon_cost : the price of the base item in Mesos, with all Upgrade slots remaining
scroll_cost : the price of the primary Dark Scroll for that item in Mesos (Dark Scrolls have a 30% chance of success, 35% chance of fail, and 35% chance of destroying the item, but give the maximum amount of stat increases)
coin_cost : the price of the secondary currency of the game (Prestigious Coins) in Mesos
trials : the number of slots on the item by default
target : the desired number of successful Scrolls passed
stop_at : the cases in which scrolling is no longer worth attempting, in the format {successes : slots} (either due to the desired output having been obtained, or any possible outputs being not worth the expected cost)
run_count : the number of simulations to attempt
four_cost : the typical price a player can expect by selling a by-product item with 4 passes
five_cost : the typical price a player can expect by selling a by-product item with 5 passes
six_cost : the typical price a player can expect by selling a by-product item with 6 passes

The program will repeatedly Scroll a base item until one of the stop_at cases is reached or there are no more remaining Upgrade slots available, at which point it will increase the number of that "finished" product that has been produced.
After the simulations are complete, the program then will print the total amount of each "finished" product, as well as calculating the total revenue that can be recouped by selling off byproducts.
Finally, the program will calculated the expected_cost of the item and print out the total cost in both Mesos and Coins as well as the expected_cost per item, in Coins.