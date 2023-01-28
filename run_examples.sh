echo "Launching Euroc Dataset with Monocular-Inertial sensor"

# euroc dataset
root=/media/psf/work/data/euroc_data
./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.bin ./Examples/Monocular-Inertial/EuRoC.yaml $root/MH_01 ./Examples/Monocular-Inertial/EuRoC_TimeStamps/MH01.txt dataset-MH01_monoi

# phone-slamdemo dataset
# root="/media/psf/work/project/20230116 slam数据采集/data"
# dataset_name=dataset-mate20_monoi
# ./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.bin ./Examples/Monocular-Inertial/mate20.yaml "$root" "$root/mav0/cam0/data.csv" $dataset_name

