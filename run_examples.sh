echo "Launching Euroc Dataset with Monocular-Inertial sensor"

# euroc dataset
# root=/media/psf/work/data/euroc_data
# ./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.bin ./Examples/Monocular-Inertial/EuRoC.yaml $root/MH_01_easy ./Examples/Monocular-Inertial/EuRoC_TimeStamps/MH01.txt dataset-MH01_monoi

# phone-slamdemo dataset
root="/media/psf/work/data/slam/mate20/dataset/indoor_walking_loop_staticinit_2"
dataset_name=dataset-mate20_monoi
# ./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.bin ./Examples/Monocular-Inertial/mate20-640.yaml "$root" "$root/mav0/cam0/timestamp.csv" $dataset_name
./Examples/Monocular/mono_euroc ./Vocabulary/ORBvoc.bin ./Examples/Monocular-Inertial/mate20-640.yaml "$root" "$root/mav0/cam0/timestamp.csv" $dataset_name
