# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = D:\SoftwareInstallation\CMake\bin\cmake.exe

# The command to remove a file.
RM = D:\SoftwareInstallation\CMake\bin\cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = D:\Learning\Leetcode_solution

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = D:\Learning\Leetcode_solution\build

# Include any dependencies generated for this target.
include CMakeFiles/AlgorithmLearning.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/AlgorithmLearning.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/AlgorithmLearning.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/AlgorithmLearning.dir/flags.make

CMakeFiles/AlgorithmLearning.dir/main.cpp.obj: CMakeFiles/AlgorithmLearning.dir/flags.make
CMakeFiles/AlgorithmLearning.dir/main.cpp.obj: D:/Learning/Leetcode_solution/main.cpp
CMakeFiles/AlgorithmLearning.dir/main.cpp.obj: CMakeFiles/AlgorithmLearning.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=D:\Learning\Leetcode_solution\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/AlgorithmLearning.dir/main.cpp.obj"
	D:\SoftwareInstallation\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/AlgorithmLearning.dir/main.cpp.obj -MF CMakeFiles\AlgorithmLearning.dir\main.cpp.obj.d -o CMakeFiles\AlgorithmLearning.dir\main.cpp.obj -c D:\Learning\Leetcode_solution\main.cpp

CMakeFiles/AlgorithmLearning.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/AlgorithmLearning.dir/main.cpp.i"
	D:\SoftwareInstallation\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E D:\Learning\Leetcode_solution\main.cpp > CMakeFiles\AlgorithmLearning.dir\main.cpp.i

CMakeFiles/AlgorithmLearning.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/AlgorithmLearning.dir/main.cpp.s"
	D:\SoftwareInstallation\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S D:\Learning\Leetcode_solution\main.cpp -o CMakeFiles\AlgorithmLearning.dir\main.cpp.s

# Object files for target AlgorithmLearning
AlgorithmLearning_OBJECTS = \
"CMakeFiles/AlgorithmLearning.dir/main.cpp.obj"

# External object files for target AlgorithmLearning
AlgorithmLearning_EXTERNAL_OBJECTS =

AlgorithmLearning.exe: CMakeFiles/AlgorithmLearning.dir/main.cpp.obj
AlgorithmLearning.exe: CMakeFiles/AlgorithmLearning.dir/build.make
AlgorithmLearning.exe: CMakeFiles/AlgorithmLearning.dir/linkLibs.rsp
AlgorithmLearning.exe: CMakeFiles/AlgorithmLearning.dir/objects1
AlgorithmLearning.exe: CMakeFiles/AlgorithmLearning.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=D:\Learning\Leetcode_solution\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable AlgorithmLearning.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\AlgorithmLearning.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/AlgorithmLearning.dir/build: AlgorithmLearning.exe
.PHONY : CMakeFiles/AlgorithmLearning.dir/build

CMakeFiles/AlgorithmLearning.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\AlgorithmLearning.dir\cmake_clean.cmake
.PHONY : CMakeFiles/AlgorithmLearning.dir/clean

CMakeFiles/AlgorithmLearning.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" D:\Learning\Leetcode_solution D:\Learning\Leetcode_solution D:\Learning\Leetcode_solution\build D:\Learning\Leetcode_solution\build D:\Learning\Leetcode_solution\build\CMakeFiles\AlgorithmLearning.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/AlgorithmLearning.dir/depend

