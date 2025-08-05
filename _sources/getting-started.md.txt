# Getting started

This section provides a comprehensive guide for customers on how to unbox and begin using the product upon delivery.

## First step

Please open the package and inspect the vehicle and accompanying items immediately upon delivery.

### Hardware checklist

|    |  Item           | Quantity         |    |  Item           | Quantity          |
|----|-------------|----------|----|-------------|----------|
|  ☐  | Main LiDAR        | 1 |  ☐  | Brake pedal | 1 |
|  ☐  | Blind-spot LiDAR  | 2 |  ☐  | Steering wheel | 1 |
|  ☐  | TIER IV C2 Camera | 2 |  ☐  | Driver panel | 1 |
|  ☐  | Ultrasonic radar  | 8 |  ☐  | Seats | 2 |
|  ☐  | **Long range radar** | 1 |  ☐  | Canopy | 1 |
|  ☐  | GNSS antenna | 2 |  ☐  | Bumper | 2 |
|  ☐  | Integrated navigation system | 1 |  ☐  | Headlight | 2 |
|  ☐  | Computing unit | 1 |  ☐  | Front Turn Signal Light | 2 |
|  ☐  | **Sub computing unit** | **1** |  ☐  | Rear Turn Signal Light | 2 |
|  ☐  | Chassis | 1 |  ☐  | Brake Light | 2 |
|  ☐  | Side mirror | 2 |  ☐  | 15.6-inch Monitor | 1 |
|  ☐  | Accelerator pedal | 1 |

%|  13  | Brake pedal | 1 |
%|  14  | Steering wheel | 1 |
%|  15  | Driver panel | 1 |
%|  16  | Seats | 2 |
%|  17  | Canopy | 1 |
%|  18  | Bumper | 2 |
%|  19  | Headlight | 2 |
%|  20  | Front Turn Signal Light | 2 |
%|  21  | Rear Turn Signal Light | 2 |
%|  22  | Brake Light | 2 |
%|  23  | 15.6-inch Monitor | 1 |

### Accessories checklist

|    |  Item           | Quantity         |    |  Item           | Quantity          |
|----|-------------|----------|----|-------------|----------|
|  ☐  | Chassis charger        | 1 |  ☐  | Certificate of conformity  | 1 |
|  ☐  | Remote controller        | 1 |  ☐  | Warranty document    | 1 |
|  ☐  | User manual        | 1 |  ☐  | Delivery packing list       | 1 |
|  ☐  | Accessory set       | 1 |    | | 

```{important}
- Check for any damage during transportation of the kit.
- Check items against the packing list for missing, misdelivered, or mismatched accessories/documents.
```
<br />
  
![Remote controller](images/dtvk_doc_02.png)

## Remote controller

The industrial remote controller is a crucial component for operating the vehicle. Familiarize yourself with the functions of each switch before use.

| #  | Controller functions   | Details |
|----| -----------------------|-------------|
| 1  | Power button           | Turns controller on and off |
| 2  | Throttle/brake         | Adjusts speed and braking |
| 3  | Gear selector          | Selects gear mode (D/N/R) |
| 4  | Headlights             | Turns headlights on and off |
| 5  | Handbrake              | Toggles parking brake |
| 6  | Control mode           | Switches between remote control and autonomous mode |
| 7  | Steering mode          | Selects steering mode |
| 8  | Steering control       | Controls the vehicle's steering direction |
| 9  | Motor control mode     | Selects motor control mode |
| 10 | Speed limiter          | Toggles speed limiter |
| 11 | Drive mode (2WD/4WD)   | Selects two-wheel and four-wheel drive modes |
| 12 | Emergency stop         | Brings vehicle to a halt in event of emergency |
| 13 | Display view           | Switches display page on LCD panel |
| 14 | Remote controller lock | Locks controller to prevent unauthorized use |

### LCD Panel
The LCD panel on the remote controller displays both the remote controller's status and the vehicle's status. 

<p>
  <span class="highlight-text">
    For details on fault codes displayed on the remote controller and suggested troubleshooting steps, please refer to the relevant section in the manual.
  </span>
</p>

![Remote controller display](images/dtvk_doc_03.png)

| #  | Display indicators        |
|----|---------------------------|
| 1  | Controller battery status |
| 2  | Signal strength           |
| 3  | Button feedback           |
| 4  | Control mode              |
| 5  | Steering mode             |
| 6  | Steering range            |
| 7  | Vehicle battery status    |                            
| 8  | Speed mode                |
| 9  | Control mode              |
| 10 | Drive mode                |
| 11 | Speed                     |
| 12 | Throttle/braking range    |
| 13 | Gear status               |

### Safety tips for teleoperation
Users must familiarize themselves with the remote controller before entering autonomous driving mode, especially the emergency stop function.

- When turning the remote controller on and off, ensure that all function buttons are in the off state, for example, parking, neutral gear, remote control mode, and no throttle.
- Verify that all buttons are functional before operating the vehicle.
- When in remote control mode, do not push the throttle to its maximum level in one go to avoid potential accidents. Throttle control should be gradually applied.
- When operating in an open area, ensure that the remote controller’s working range does not exceed 100 meters.
- After stopping the vehicle, ensure that the vehicle is in neutral gear and the handbrake is engaged. Avoid parking on slopes.
- Users must must carefully read the instructions before use. People unfamiliar with the controls should not operate the vehicle, as this may result in accidents.

Both the remote controller system and the vehicle’s VCU layer assign absolute priority to the remote control receiver. <span class="highlight-text">And the basic rule is that under any condition of the vehicle’s chassis (ensure the remote controller is charged before each operation), as long as the remote controller is powered on and in remote takeover mode, the vehicle chassis will enter manual takeover mode.</span> This ensures safety during development and testing.

## Vehicle startup procedure

### 1. Power on the chassis
Please refer to the button descriptions in the diagram below. Press the power switch on the control panel to power on the vehicle.

![Cockpit](images/dtvk_doc_05.png)

<br />

| #  | Cockpit controls               | Details |
|----| -----------------------|-------------|
| 1  | Steering wheel          | Only operational in manual driving mode |
| 2  | Brake pedal         | Only operational in manual driving mode |
| 3  | Throttle pedal         | Only operational in manual driving mode |
| 4  | Gear switch knob             | Only operational in manual driving mode |
| 5  | Emergency stop button  | Toggles emergency stop on and off|
| 6  | Park button         | Only operational in manual driving mode|
| 7  | Manual mode button  | See **Manual mode** |
| 8  | Power button       | Vehicle start/shut down |


```{attention}
<span class="highlight-text"> If the emergency stop button is activated, the vehicle chassis will not respond to any control commands, regardless of the vehicle being in teleoperation mode, manual mode, or autonomous driving mode. </span>
```

### 2. Handbrake Confirmation
Ensure the handbrake lever on the industry remote control is in the "Handbrake On" (engaged) position.

![Handbrake lever](images/dtvk_doc_06.png)

### 3. Turning on the remote controller
Rotate the power switch knob on the remote controller to the “On” position.

```{attention}
If the remote controller emits a beeping sound, it indicates that the communication betwen the controller and the chassis has not been established. Please wait until the chassis power system is fully activated and the beeping stops before proceeding.
```
<br />

![Controller power up](images/dtvk_doc_06.png)

### 4. Gear selection
Rotate the gear switch knob on the remote controller and select reverse gear.

![Reverse gear selected](images/dtvk_doc_06.png)

### 5. Braking
Push the left lever all the way down to engage full braking force (100%).

![Throttle/brake lever](images/dtvk_doc_06.png)

### 6. Releasing the handbrake
While holding the left lever fully down in the braking position, switch the handbrake control to **Handbrake Off**.
Once you hear the sound of the handbrake releasing, slowly release the left lever, allowing the vehicle to roll off the trailer.

```{caution}
Monitoring the vehicle's rolling speed closely. If it becomes too fast or there is any risk of collision, push the left lever down to brake immediately.
```

### 7. Parking
Once the vehicle has rolled to a full stop on the ground, switch the handbrake control back to **Handbrake On**.
