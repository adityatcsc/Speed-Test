
import speedtest

def run_speed_test():
    st = speedtest.Speedtest()
    
    print("Getting the best server...")
    st.get_best_server()
    
    print("Testing download speed...")
    download_speed = st.download() / 10**6  # Convert from bits per second to megabits per second
    print(f"Download speed: {download_speed:.2f} Mbps")
    
    print("Testing upload speed...")
    upload_speed = st.upload() / 10**6  # Convert from bits per second to megabits per second
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print("Ping ",st.results.ping)

if __name__ == "__main__":
    run_speed_test()
