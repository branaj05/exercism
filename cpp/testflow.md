cd cpp\lasagna
mkdir build
cd build
cmake ..
cmake --build .

# MAC
        
    cd cpp/lasagna
    mkdir -p build
    cd build
    DO:
        cmake -DEXERCISM_RUN_ALL_TESTS=ON ..
    OR
        cmake -DCMAKE_BUILD_TYPE=Debug -DEXERCISM_RUN_ALL_TESTS=ON ..
    Then:
    cmake --build .
