---
layout: post
title: How to write a phonological rule in Microsoft Word
tags: phonology, tools
---

The equation editor in Word allows matrices and brackets of various sizes, which is 90% of what we need to make a rule. 

Let us recreate the following rule from page 352 of Sound Pattern of English:

![Screenshot of rule from Sound Pattern of English page 352.](/assets/spe-rule.png)

This rule uses ɑ notation to quantify over feature values, and each part of the rule is an explicit feature matrix. 

Phonological rules in Word are created using the Equation editor, so to start, go to Insert on the ribbon, and click Equation, under the Symbols section. (The following directions are for the Windows version of Word, though the process is similar on other platforms.)

For the first feature matrix, insert a pair of square Brackets.

![Insert brackets for each feature matrix.](/assets/rule-brackets.png)

The brackets will automatically resize depending on whatever is inside. Make sure the outlined box is gray (use the arrows to move the cursor left and right until this is the case), then select Matrix, and select the 1x2 matrix. The size of the matrix will correspond to the number of features in the feature matrix. In the top element of the feature matrix, type “-son”. You will notice that it appears in a slightly italic looking style, with awkward spacing. This is because by default Word expects parts of an equation, not words. Select what you just typed, and click “Text” at the top. This tells Word that this part of the equation is plain text. (I like to leave the hyphen unchanged so it registers a true minus sign.)

![Change feature names to plain text.](/assets/rule-text.png)

Complete the feature matrix in the same way. When you need to insert the arrow in the rule, one is available in the “Symbols” window in the ribbon. When you get to the part of the rule separated by a slash “/”, you might see the equation editor interpret this as the desire to insert a fraction:

<img src="/assets/Rule%20example.gif">

If this happens, undo, and click “Text” before you type the slash. Now it will appear as expected, and you can continue adding bracketed feature matrices for the rest of the rule. Again, Word may interpret the underscore as a subscripted element, so be sure to hit Text before typing the underscore as well. I used a sequence of three underscores in my final version of the rule, shown below:

![Image of final rule, with the slash and underscore as plain text.](/assets/rule-final.png)

The rule now exists as an Equation. If you want it to look more like the original SPE rule, you can change the justification of the Matrix elements to be left-aligned instead of centered by right-clicking an element in a matrix and choosing Left from Column Alignment:

![Change column alignment to better match visually the original rule.](/assets/rule-alignment.png)

Moving forward, you might want to create a rule template that you will use often. To do so, select “Save as New Equation” after clicking the arrow in the bottom-right corner of the equation border. 

![Save rule template to the Equations gallery.](/assets/rule-save.png)

Now, you can insert the rule with a single click from the Equations gallery accessible from the Equation ribbon.

![Select rule from the Equations gallery for easy insertion next time.](/assets/rule-saved.png)

As Equations, the rules can be shown centered on their own lines, or inline with text. Learning the general properties of the Equation editor in Word will help you better incorporate the rules into your work. 