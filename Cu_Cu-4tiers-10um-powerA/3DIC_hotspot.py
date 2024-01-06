import os
import time

t0 = time.time()
cmd = "../hotspot -c ../new_hotspot.config -f ./Power-Die.flp -p ./3DIC.ptrace -steady_file ./results.steady -grid_steady_file ./results.grid.steady -model_type grid -detailed_3D on -grid_layer_file ./3DIC_layers.lcf"
os.system(cmd)
t1 = time.time()
print(f"Time={t1-t0}")

# cmd = "../hotspot -c ../new_hotspot.config -f ./Power-Die.flp -p ./3DIC.ptrace -steady_file ./results.steady -grid_steady_file ./results.grid.steady -model_type grid"
# os.system(cmd)

def get_Peak_Temperature():
    Temperature = []
    with open("./results.grid.steady") as f:
        for line in f:
            ele = line.split("\t")

            cleaned_str = ''.join(char for char in ele[-1] if char.isdigit() or char == '.')
            try:
                Temperature.append(float(cleaned_str))
            except ValueError:
                print("Error: Unable to convert string to float.")

    max_Temperature = max(Temperature)
    return max_Temperature

Peak_Temperature = get_Peak_Temperature()
print(f"Peak_Temperature={Peak_Temperature}")

cmd = "../grid_thermal_map.pl ./Power-Die.flp ./results.grid.steady 64 64 > ./results.svg"
os.system(cmd)

