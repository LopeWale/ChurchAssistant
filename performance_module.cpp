#include <iostream>
#include <string>

class PerformanceModule {
public:
    // Constructor
    PerformanceModule() {
        std::cout << "PerformanceModule initialized." << std::endl;
    }

    // Method for processing audio data
    void process_audio(const std::string& audio_data) {
        std::cout << "Processing audio data: " << audio_data << std::endl;
    }
};

// Expose a C-compatible function to be used in Python via ctypes
extern "C" {
    PerformanceModule* PerformanceModule_new() {
        return new PerformanceModule();
    }
    void PerformanceModule_process_audio(PerformanceModule* pm, const char* audio_data) {
        pm->process_audio(audio_data);
    }
}


