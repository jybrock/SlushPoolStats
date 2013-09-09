#!/usr/bin/python
# based on https://github.com/pdbrown/munin-custom/blob/master/plugins/hashrate

import urllib2
import json

YOUR_SLUSH_API_KEY = ""
SLUSH_STATS = 'https://mining.bitcoin.cz/accounts/profile/json/%s' % YOUR_SLUSH_API_KEY

mining_stats_raw = urllib2.urlopen(SLUSH_STATS)
mining_stats = json.load(mining_stats_raw)

unconfirmed = float(mining_stats['unconfirmed_reward'])
estimated = float(mining_stats['estimated_reward'])
confirmed = float(mining_stats['confirmed_reward'])

totalearnings = unconfirmed+confirmed

SLUSH_STATS_POOL = 'https://mining.bitcoin.cz/stats/json/'

s2_stats_raw = urllib2.urlopen(SLUSH_STATS_POOL)
s2_stats = json.load(s2_stats_raw)

print "===================================="
print "  Round Duration: %s" % s2_stats['round_duration']
print "  Shares CDF:      %s%%" % s2_stats['shares_cdf']
print "  Estimated:   %s" % estimated
print "  Unconfirmed: %s" % unconfirmed
print "  Confirmed:   %s" % confirmed
print "  Total:       %s" % totalearnings
print "===================================="