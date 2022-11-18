class DataStream:

    def __init__(self):
        self.data_dict = {}

    def should_output_data_str(self, timestamp, data_string):
        if data_string not in self.data_dict:
            self.data_dict[data_string] = timestamp
            return True
        else:
            if timestamp > self.data_dict[data_string]+4 :
                self.data_dict[data_string] = timestamp
                return True
            else:
                return False


if __name__ == '__main__':
    final_result = []
    data_stream = DataStream()
    final_result.append(data_stream.should_output_data_str(timestamp=0, data_string='hello'))
    final_result.append(data_stream.should_output_data_str(timestamp=1, data_string='world'))
    final_result.append(data_stream.should_output_data_str(timestamp=5, data_string='hello'))
    final_result.append(data_stream.should_output_data_str(timestamp=7, data_string='hello'))
    final_result.append(data_stream.should_output_data_str(timestamp=8, data_string='world'))
    print(final_result)
