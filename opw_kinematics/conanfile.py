from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMakeToolchain


class OpwKinematicsConan(ConanFile):
    name = "opw_kinematics"
    version = "0.5.0"

    license = "Apache 2.0"
    author = "Jonathan Meyer"
    url = ""
    description = ""
    topics = ("")
    
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    requires = "ros_industrial_cmake_boilerplate/[>=0.3]@demo/testing"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        git = tools.Git(folder="opw_kinematics")
        git.clone('https://github.com/Jmeyer1292/opw_kinematics.git')
        git.checkout('0.5.0')

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="opw_kinematics")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["opw_kinematics"]
