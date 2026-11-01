#include <string>
#include <format>
namespace log_line {
std::string message(std::string line) {
    // return the message
    std::string message_delimter = ": ";
    return line.substr(line.find(message_delimter) + message_delimter.size());
}

std::string log_level(std::string line) {
    // return the log level
    size_t lvl_start = line.find("[");
    size_t lvl_end = line.find("]");
    return line.substr(lvl_start+1, lvl_end-lvl_start-1);
}

std::string reformat(std::string line) {
    // return the reformatted message
    std::string msg = message(line);
    std::string lvl = log_level(line);
    // return std::format("{} ({})", msg, lvl);
    return msg + " ("+lvl+")";
}
}  // namespace log_line
