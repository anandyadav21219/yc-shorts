// Renders one line of Devanagari text to a 1080-wide transparent PNG (CoreText shapes the conjuncts).
// usage: swift caption.swift out.png "text" [fontSize] [maxWidth]
import AppKit
let a = CommandLine.arguments
let out = a[1], text = a[2]
var size = CGFloat(a.count > 3 ? Double(a[3])! : 74)
let maxW = CGFloat(a.count > 4 ? Double(a[4])! : 950)
func attrs(_ s: CGFloat, stroke: Bool) -> [NSAttributedString.Key: Any] {
  var d: [NSAttributedString.Key: Any] = [.font: NSFont(name: "KohinoorDevanagari-Bold", size: s)!]
  if stroke { d[.strokeColor] = NSColor(white: 0.08, alpha: 0.85); d[.strokeWidth] = 14.0; d[.foregroundColor] = NSColor.clear }
  else { d[.foregroundColor] = NSColor.white }
  return d
}
while NSAttributedString(string: text, attributes: attrs(size, stroke: false)).size().width > maxW { size -= 2 }
let W = 1080, H = Int(size * 2.2)
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: W, pixelsHigh: H, bitsPerSample: 8, samplesPerPixel: 4,
  hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
let fill = NSAttributedString(string: text, attributes: attrs(size, stroke: false))
let sz = fill.size()
let p = NSPoint(x: (CGFloat(W) - sz.width) / 2, y: (CGFloat(H) - sz.height) / 2)
let sh = NSShadow(); sh.shadowColor = NSColor(white: 0, alpha: 0.45); sh.shadowBlurRadius = 10; sh.shadowOffset = NSSize(width: 0, height: -3)
NSGraphicsContext.current!.saveGraphicsState(); sh.set()
NSAttributedString(string: text, attributes: attrs(size, stroke: true)).draw(at: p)
NSGraphicsContext.current!.restoreGraphicsState()
fill.draw(at: p)
NSGraphicsContext.restoreGraphicsState()
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: out))
print("\(out) size=\(size) h=\(H)")
