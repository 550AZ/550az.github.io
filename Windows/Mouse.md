# Mouse Settings

## Mouse Scroll Direction
If you use a mouse in Windows, the Settings app doesn't include an option o reverse the scrolling direction. However, you can still modify the scrolling behavior in Registry.

### Identifying Mouse Information
1. Open **Muse Settings**.
1. Click **Additional mouse settings** to open **Mouse Properties** window.
1. Click **Hardware** tab. Click **Properties** button to open **HID-compliant mouse Properties** window.
1. Click **Details** tab. Select **Device instance path** in **Property** list.
1. Remember the **Value**. Such as HID\VID_413C&PID_301A\6&37153F64&0&0000.

### Reverse Mouse Scrolling Direction

1. Open **Registry Editor**
2. Browse to **Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\HID**
3. Select VID of your mouse as above.
4. Select **Device Parameters**.
5. Select **FlipFlopWheel**.
6. Change Value data from **0** to **1**.