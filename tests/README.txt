Add your own test cases here.

==================================
Test Case 1 - Premium Ultrabook 
----------------------------------

Input Facts; 
    [
      "budget_high",
      "portable",
      "long_battery"
    ]

Expected Recommendation: 
 Recommend: Premium_ultrabook

Expected Specations: 
 (None)


==================================
Test Case 2 - student light Laptop 
----------------------------------

Input Facts; 
    [
      "portable",
      "budget_low",
      "office_only"
    ]

Expected Recommendation: 
 Recommend Laptop: budget_ultrabook

Expected Specations: 
 (None)


==================================
Test Case 3 - Gaming Laptop
----------------------------------

Input Facts; 
    [
      "budget_low",
      "gaming"
    ]

Expected Recommendation: 
 Recommend Laptop: midrange_gaming_laptop

Expected Specations: 
 (None)

==================================
Test Case 4 - Pro-Gaming Laptop
----------------------------------

Input Facts; 
    [
      "budget_high",
      "gaming"
    ]

Expected Recommendation: 
 Recommend Laptop: high_end_gaming_laptop

Expected Specations: 
 (None)

==================================
Test Case 5 - creative work(portable)
----------------------------------

Input Facts; 
    [
      "creative_work",
      "portable"
    ]

Expected Recommendation: 
 Recommend Laptop: default_laptop_model(no specific recommendation)

Expected Specations: 
 Specifications suggested based on prority:ram_16_plus

==================================
Test Case 5 - creative work(Display)
----------------------------------

Input Facts; 
    [
      "creative_work",
      "large_screen"
    ]

Expected Recommendation: 
 Recommend Laptop: default_laptop_model(no specific recommendation)

Expected Specations: 
 Specifications suggested based on prority: display_15_plus_color_accurate

==================================
Test Case 6 - Travel and long battery
----------------------------------

Input Facts; 
    [
      "travel_often",
      "long_battery"
    ]

Expected Recommendation: 
 Recommend Laptop: default_laptop_model(no specific recommendation)

Expected Specations: 
Specifications suggested based on prority: battery_60wh_plus
 
==================================
Test Case 7 - OS preference
----------------------------------

Input Facts; 
    [
      "pref_os_macos"
    ]

Expected Recommendation: 
 Recommend Laptop: default_laptop_model(no specific recommendation)

Expected Specations: 
 Specifications suggested based on prority: macos_required


==================================
Test Case 8 - AI Accleration
----------------------------------

Input Facts; 
    [
      "needs_ai_accel",
      "professional_software"
    ]

Expected Recommendation: 
 Recommend Laptop: default_laptop_model(no specific recommendation)

Expected Specations: 
 Specifications suggested based on prority: gpu_with_tensor_cores

==================================
Test Case 9 - Linux suitability
----------------------------------

Input Facts; 
    [
      "pref_os_linux",
      "office_only"
    ]

Expected Recommendation: 
 Recommend Laptop: default_laptop_model(no specific recommendation)

Expected Specations: 
 Specifications suggested based on prority: linux_friendly_hw

==================================
Test Case 10 - All case being None(empty)
----------------------------------

Input Facts; 
    [
      " "
    ]

Expected Recommendation: 
 Recommend Laptop: default_laptop_model(no specific recommendation)

Expected Specations: 
 (None)

==================================
Test Case 10 - All case being Yes
----------------------------------

Input Facts; 
    [
      "portable",
      "long_battery"
      "budget_low",
      "office_only"
      "gaming"
      "creative_work"
      "large_screen"
      "travel_often",
      "long_battery"
      "pref_os_macos"
      "needs_ai_accel"
    ]

Expected Recommendation: 
  Recommend Laptop: midrange_gaming_laptop

  Explanation : derived from rule 'Student light Laptop'

Expected Specations: 
Specifications suggested based on prority:

battery_60wh_plus
macos_required
gpu_with_tensor_cores
ram_16_plus
display_15_plus_color_accurate






