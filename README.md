# ACTIONPACKED

How 2 make a .apack file

Example script:
```
// Example .apack Script
// This script automates the process of opening a web browser,
// navigating to a website, clicking buttons, and checking pixel colors.

// Move the mouse to the specified coordinates (100, 200) and click
move(100, 200); // Move mouse to (100, 200)
lmb;             // Perform a left mouse button click

// Wait for 1 second to ensure the browser loads
wait(1);        // Pause for 1 second

// Move to the address bar and click to focus
move(300, 50);  // Move mouse to the address bar location
lmb;             // Click to focus on the address bar

// Type a website URL
presskey_t;     // Press 'T' to start typing
presskey_w;     // Press 'W'
presskey_i;     // Press 'I'
presskey_t;     // Press 'T'
presskey_c;     // Press 'C'
presskey_h;     // Press 'H'
presskey_dot;   // Press '.'
presskey_t;     // Press 'T'
presskey_v;     // Press 'V'

// Wait for the website to load
wait(2);        // Pause for 2 seconds

// Click on a specific button on the page
move(400, 300); // Move mouse to the button location
lmb;             // Click the button

// Wait for the action to complete
wait(1);        // Pause for 1 second

// Check if a pixel at (500, 400) is white (RGB 255, 255, 255)
checkrgb(255, 255, 255, 500, 400):[
    presskey_enter; // If the pixel is white, press the Enter key
    wait(0.5);      // Wait for half a second
];

// Repeat a specific action multiple times
repeat(3):[
    move(600, 200); // Move to another coordinate
    lmb;            // Click
    wait(1);        // Wait for a second between clicks
];

// Define a variable for the mouse position
var [current_x, 100]; // Initialize a variable to hold the current x position
var [current_y, 200]; // Initialize a variable to hold the current y position

// Move to the variable positions and click
move(current_x, current_y); // Move to (100, 200)
lmb;                         // Click at that position

// Multi-line comment to describe the next actions
// [ Start of multi-line comment
// The following section demonstrates using a function
// to group similar actions together.
// ]
func clickAndWait():[
    lmb;       // Click
    wait(0.5); // Wait for half a second
];

// Call the function to perform its actions
clickAndWait(); // Call the function
clickAndWait(); // Call it again to demonstrate repetition

// End of the script

// Btw pls dont run this. This is just an example.
```
