#import "ViewController.h"
#import <Metal/Metal.h>
#import <QuartzCore/CAMetalLayer.h>
#import "engine.h"

@implementation ViewController {
    id<MTLDevice> device;
    id<MTLCommandQueue> queue;
    id<MTLLibrary> library;
    id<MTLRenderPipelineState> pipeline;
    CAMetalLayer *layer;
}

+ (Class)layerClass {
    return [CAMetalLayer class];
}

- (void)viewDidLoad {
    [super viewDidLoad];

    device = MTLCreateSystemDefaultDevice();
    queue = [device newCommandQueue];

    layer = (CAMetalLayer *)self.view.layer;
    layer.device = device;
    layer.pixelFormat = MTLPixelFormatBGRA8Unorm;

    library = [device newDefaultLibrary];

    MTLRenderPipelineDescriptor *desc = [[MTLRenderPipelineDescriptor alloc] init];
    desc.vertexFunction = [library newFunctionWithName:@"vertex_main"];
    desc.fragmentFunction = [library newFunctionWithName:@"fragment_main"];
    desc.colorAttachments[0].pixelFormat = MTLPixelFormatBGRA8Unorm;

    pipeline = [device newRenderPipelineStateWithDescriptor:desc error:nil];

    engine_init();
    [self drawLoop];
}
- (void)drawLoop {
    @autoreleasepool {
        id<CAMetalDrawable> drawable = [layer nextDrawable];
        if (!drawable) return;

        MTLRenderPassDescriptor *pass = [MTLRenderPassDescriptor renderPassDescriptor];
        pass.colorAttachments[0].texture = drawable.texture;
        pass.colorAttachments[0].loadAction = MTLLoadActionClear;
        pass.colorAttachments[0].clearColor = MTLClearColorMake(0.1, 0.1, 0.15, 1);
        pass.colorAttachments[0].storeAction = MTLStoreActionStore;

        id<MTLCommandBuffer> buffer = [queue commandBuffer];
        id<MTLRenderCommandEncoder> enc = [buffer renderCommandEncoderWithDescriptor:pass];

        [enc setRenderPipelineState:pipeline];
        [enc drawPrimitives:MTLPrimitiveTypeTriangle vertexStart:0 vertexCount:3];
        [enc endEncoding];

        [buffer presentDrawable:drawable];
        [buffer commit];

        engine_update(1.0f / 60.0f);
    }

    dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 16 * NSEC_PER_MSEC),
                   dispatch_get_main_queue(), ^{
        [self drawLoop];
    });
}