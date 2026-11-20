import CoreImage
import AppKit
let url = URL(fileURLWithPath: CommandLine.arguments[1])
let img = CIImage(contentsOf: url)!
let det = CIDetector(ofType: CIDetectorTypeQRCode, context: nil, options: [CIDetectorAccuracy: CIDetectorAccuracyHigh])!
let fs = det.features(in: img)
if fs.isEmpty { print("NO_QR") }
for f in fs { if let q = f as? CIQRCodeFeature { print("READ:", q.messageString ?? "nil") } }
