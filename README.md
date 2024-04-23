# Python File Transfer Application

This Python-based file transfer application allows users to transfer files between a server and multiple clients using socket programming.

## Screenshots

![Home page](https://github.com/PurnimaCoder/GitaShare/blob/main/images/Screenshot%20(26).png)
![Send page](https://github.com/PurnimaCoder/GitaShare/blob/main/images/Screenshot%20(27).png)
![Recieve page](https://github.com/PurnimaCoder/GitaShare/blob/main/images/Screenshot%20(31).png)

## Features

- **Client-Server Architecture**: Utilizes a client-server model for file transfer.
- **File Transfer**: Enables users to send and receive files between the server and clients.
- **Concurrency**: Supports multiple clients connecting to the server simultaneously.
- **Error Handling**: Implements error handling to ensure reliable file transfer.

## Technologies Used

- **Python**: Programming language used for implementation.
- **Socket Programming**: Leveraged for network communication between server and clients.

## Usage

### Server

1. Run the server script on the host machine:

   ```bash
   python server.py

2. The server will start listening for incoming connections.

### Client

1. Run the client script on the client machine:

   ```bash
   python client.py

2. Enter the server's IP address and port number when prompted.
   
3. Follow the on-screen instructions to send or receive files.

## Configuration

**Server Configuration**: Modify the server configuration parameters (e.g., host, port) in ```server.py``` if necessary.

**Client Configuration**: Adjust the client configuration parameters (e.g., server IP address, port) in ```client.py``` as needed.

## Notes

1. Ensure that both the server and client machines are on the same network for successful communication.
2. Verify that the specified port is not blocked by any firewall settings.
3. File transfer speed may vary depending on network conditions and file size.
4. Error messages will be displayed in case of any connection issues or file transfer failures.

## License

This project is licensed under the MIT License.

```vbnet
Feel free to customize the content as needed, such as adding more detailed instructions, usage examples, or configuration options based on your specific implementation.

