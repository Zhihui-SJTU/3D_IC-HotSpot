#!/bin/bash

# You can add more settings depends on your own tasks such as memory limit
#SBATCH -J 3DIC_hotspot		# Job name
#SBATCH -p CLUSTER			# choose the partition "gpu" or "CLUSTER"
#SBATCH -o %j.out		# output file
#SBATCH -e %j.err		# error file
#SBATCH --ntasks-per-node=1	# number of cores for the task
#SBATCH -N 1			# number of node for the task
#SBATCH --nodelist=node1	# choose the specific node for the task. in "gpu" we only have one node

# Automatically detect the GPU with more computational resources
FREE_GPU=$(nvidia-smi --query-gpu=memory.free --format=csv,noheader | awk -F "[ ,]" '{print $1 " " NR-1}' | sort -nr | head -n 1 | awk '{print $2}')
export CUDA_VISIBLE_DEVICES=$FREE_GPU

# default is "cd .", all the output files will be saved in this path
cd /home/zhihui/Desktop/code/140/code/workspace/Chiplet_placement_order/chiplet_new2/main/3DIC_hotspot/Cu_pillar-8tiers-50um-powerB/

# activate your conds env
source /home/fwtop/anaconda3/bin/activate torch2.0

# Execute your script
python -u /home/zhihui/Desktop/code/140/code/workspace/Chiplet_placement_order/chiplet_new2/main/3DIC_hotspot/Cu_pillar-8tiers-50um-powerB/3DIC_hotspot.py
