# Connecting Brilliant Labs Frame Glasses to Windows 11

This technical guide provides detailed instructions for establishing a Bluetooth connection between Brilliant Labs Frame glasses and a Windows 11 computer.

## System Requirements

### Hardware
- Brilliant Labs Frame glasses
- Mister Power charging adapter
- USB-C cable
- Pin tool or SIM card ejector
- Windows 11 computer with Bluetooth capability

### Technical Prerequisites
- Windows 11 with latest Bluetooth drivers
- Bluetooth Low Energy (BLE) support
- No existing Frame device pairings

## Connection Process

### Phase 1: Device Reset
1. Hardware Setup
   - Connect the Mister Power adapter to Frame glasses
   - Attach USB-C cable to power source
   - Locate the reset pinhole beneath the Mister Power indicator LED

2. Reset Procedure
   - Insert pin tool into reset aperture
   - Apply gentle pressure for exactly 3 seconds
   - Release pin
   - System will initiate reset sequence

3. Reset Verification
   - Don the Frame glasses
   - Execute single tap gesture
   - Observe prism display
   - Confirm "Frame" text visualization

### Phase 2: Windows 11 Configuration
1. Access System Settings
   ```
   Settings -> Bluetooth & devices
   ```

2. Bluetooth Preparation
   - Enable Bluetooth subsystem
   - Clear existing Frame device entries
   - Verify Bluetooth discovery mode

### Phase 3: Pairing Protocol
1. Initiate Device Addition
   - Select "Add device"
   - Choose "Bluetooth" protocol
   - Enter device discovery mode

2. Device Recognition
   - Monitor available devices list
   - Identify Frame device entry
   - Select Frame from device roster

3. Connection Establishment
   - Acknowledge pairing request
   - Wait for bonding completion
   - Verify BLE connection status

### Phase 4: Connection Validation
1. System Verification
   - Confirm Frame appears in paired devices
   - Verify connection status indicator
   - Test basic communication
      - Error when not connected:
   ```
      device: Any = filtered_list[0][0]
      IndexError: list index out of range
   ```

2. Troubleshooting Criteria
   - If connection fails:
     - Repeat reset procedure
     - Clear all previous pairings
     - Restart pairing sequence

## Technical Notes

- Frame utilizes BLE bonding protocol
- Complete pairing sequence required for communication
- Maintain close proximity during initial pairing
- Optimal performance requires clear line of sight between devices

## Reference Architecture
Frame implements standard Bluetooth 5.0 LE protocol with the following specifications:
- Bonding required for secure communication
- Low latency data transmission
- Power-optimized connection management

---
*Last Updated: January 2025*