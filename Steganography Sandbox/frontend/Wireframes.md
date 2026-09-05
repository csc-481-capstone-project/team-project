# Steganography Sandbox Wireframes

## Shared Navigation

```text
+-------------------------------------------------------------------+
| Stego Sandbox | Home | Embed | Extract | Reports | About          |
+-------------------------------------------------------------------+
```

## Home Page

```text
+-------------------------------------------------------------------+
|                  Steganography Sandbox                            |
|      An educational environment for secure stego experiments.     |
|                                                                   |
| [ Start an Embed Experiment ]   [ Extract a Hidden Message ]      |
|                                                                   |
| Supported carriers:  [ Image LSB ] [ Audio LSB ] [ Zero-Width ]  |
|                                                                   |
| Educational-use notice: Do not use this application to conceal   |
| harmful, illegal, or unauthorized content.                       |
+-------------------------------------------------------------------+
```

## Embed Page

```text
+-------------------------------------------------------------------+
| Embed a Secret Message                                             |
|                                                                   |
| Carrier type:       ( Image v )                                   |
| Upload carrier:     [ Choose File ]                               |
| Secret message:     [_______________________________]            |
| Passphrase:         [_______________________________]            |
|                                                                   |
| [ Start Embed Experiment ]                                        |
|                                                                   |
| Validation and helpful error messages appear here.                |
+-------------------------------------------------------------------+
```

## Extract Page

```markdown
+-------------------------------------------------------------------+
| Extract a Hidden Message                                           |
|                                                                   |
| Carrier type:       ( Image v )                                   |
| Upload encoded file:[ Choose File ]                               |
| Passphrase:         [_______________________________]            |
|                                                                   |
| [ Start Extract Experiment ]                                      |
|                                                                   |
| Validation and helpful error messages appear here.                |
+-------------------------------------------------------------------+
```

## Job Status Page

```markdown
+-------------------------------------------------------------------+
| Experiment Status                                                  |
|                                                                   |
| Experiment ID: 12345                                               |
| Carrier: Image                                                     |
| Operation: Embed                                                   |
|                                                                   |
| Status: Processing                                                 |
| [======================------] 75%                                |
|                                                                   |
| Current step: Generating analysis results                         |
|                                                                   |
| [ Cancel Experiment ]                                             |
+-------------------------------------------------------------------+
```

## Results Page

```markdown
+-------------------------------------------------------------------+
| Experiment Results                                                 |
|                                                                   |
| Status: Complete                                                   |
| Carrier: Image LSB                                                 |
| Detection summary: Minor statistical variation detected.          |
|                                                                   |
| [ Visualization / Histogram Area ]                                |
|                                                                   |
| [ Download Output File ] [ Download PDF Report ]                  |
| [ Start Another Experiment ]                                      |
+-------------------------------------------------------------------+
```

## Error State

```markdown
+-------------------------------------------------------------------+
| Upload Error                                                       |
|                                                                   |
| The selected file type is not supported.                           |
| Please upload a PNG image, WAV audio file, or supported text file.|
|                                                                   |
| [ Return to Experiment Form ]                                     |
+-------------------------------------------------------------------+
```