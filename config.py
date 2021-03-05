Host = "http://localhost:4723/wd/hub"

Desired_Capabilities = {
    "deviceName": "Android Emulator",
    "platformName": "Android",
    "appPackage": "com.google.android.calculator",
    "appWaitActivity": "com.android.calculator2.Calculator",
    "app": "C:\\Users\\avira\\OneDrive\\Desktop\\com.google.android.calculator_v7.7-256466574-77000103_Android-6.0.apk"
}

Digit_ID = "com.google.android.calculator:id/digit_"

Operator_ADD_ID = "com.google.android.calculator:id/op_add"
Operator_Equal_ID = "com.google.android.calculator:id/eq"

Result_ID = "com.google.android.calculator:id/result_final"