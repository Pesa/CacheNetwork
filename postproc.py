#!/usr/bin/env python

import argparse, pickle

parser = argparse.ArgumentParser(description='Postprocess output files.')
parser.add_argument('filename', type=str, help='pickled file to be processed')
args = parser.parse_args()

with open(args.filename, 'rb') as f:
    sim_args, construct_stats, optimal_stats, demand_stats, node_stats, network_stats = pickle.load(f)

F = optimal_stats['F']
print("F = %.9f\n" % optimal_stats['F'])

times1 = sorted(network_stats['fun'].keys())[1:]
times2 = sorted(network_stats['demand'].keys())[1:]
if times1 != times2:
    raise RuntimeError("Time points are different")

ecg_list = [ network_stats['fun'][t][0] for t in times1 ]
tot = network_stats['fun'][times1[0]][3]
tacg_list = [ tot - network_stats['demand'][t]['weight'] for t in times2 ]

print("    Time        ECG        TACG")
for row in zip(times1, ecg_list, tacg_list):
    print("%.9f %.9f %.9f" % row)
