import CoreImage
import AppKit
let s = CommandLine.arguments[1]
let f = CIFilter(name: "CIQRCodeGenerator")!
f.setValue(s.data(using: .utf8), forKey: "inputMessage")
f.setValue("Q", forKey: "inputCorrectionLevel")
let img = f.outputImage!
let ctx = CIContext()
let cg = ctx.createCGImage(img, from: img.extent)!
let rep = NSBitmapImageRep(cgImage: cg)
for y in 0..<rep.pixelsHigh {
  var line = ""
  for x in 0..<rep.pixelsWide { line += (rep.colorAt(x: x, y: y)!.brightnessComponent < 0.5) ? "1" : "0" }
  print(line)
}
