import pytest
from notification import app


def test_lambda_handler1(apigw_event1):
    ret = app.handler(apigw_event1, "")
    assert ret.get('statusCode') == 200


@pytest.fixture()
def apigw_event1():
    return {
        'pathParameters': {
            'id': '1956576f-c82a-49d3-b23e-0eb9c5dde718'
        },
        'body': '{"status":{"code":200,"http":"Fetched (selfPing) 200 600 and parsed 1/48 entries","nextFetch":1537379673,"entriesCountSinceLastMaintenance":1,"velocity":2.9,"title":"Daring Fireball","period":600,"lastFetch":1537379073,"lastParse":1537379073,"lastMaintenanceAt":1537364634,"feed":"https://daringfireball.net/feeds/main"},"permalinkUrl":"https://daringfireball.net/","standardLinks":{"alternate":[{"title":"Daring Fireball","href":"https://daringfireball.net/","rel":"alternate","type":"text/html"}],"self":[{"title":"Daring Fireball","href":"https://daringfireball.net/feeds/main","rel":"self","type":"application/atom+xml"}]},"title":"Daring Fireball","updated":1537379005,"id":"https://daringfireball.net/feeds/main","items":[{"id":"tag:daringfireball.net,2018://1.35165","published":1537378746,"updated":1537379005,"title":"★ Apple Watch Series 4","summary":"The Series 4 Apple Watch is defined by being a nicer watch.","content":"<p>Tim Cook opened the Apple Watch segment of the event last week by stating that Apple Watch wasn&#8217;t just the number one smart watch in the world (come on, that&#8217;s obvious), but that &#8220;it&#8217;s the number one watch, period&#8221;, standing in front of <a href=\\"https://daringfireball.net/misc/2018/09/series-4-review/cook-number-one.jpg\\">a slide with a big &#8220;#1&#8221; on it</a>.</p>\\n\\n<p>Number one by what measure, though? They didn&#8217;t say, which I find irksome. Presumably Cook meant number one by revenue. At last year&#8217;s event he noted revenue specifically, <a href=\\"https://www.businessinsider.com/how-the-apple-watch-just-became-the-number-one-watch-in-the-world-2017-9\\">mentioning that Apple Watch had surpassed Rolex</a>.</p>\\n\\n<p>Apple has several products that lead their markets in revenue or profit. What makes Apple Watch different from every other product the company makes, though, is a measure near and dear to the company&#8217;s soul by which they cannot claim Apple Watch to be number one: <em>nicest</em>.</p>\\n\\n<p><em>Nicest</em> is inherently subjective, of course. But iPhone, iPad, MacBook, and iMac can all reasonably be argued to be the nicest products in their respective markets. You can definitely add Apple Watch to that list if you limit the comparison to other smart watches and fitness trackers. I would say hands-down, no question, Apple Watch is the nicest of those. But that&#8217;s like saying you&#8217;re the richest person in the poorhouse. And Tim Cook is the one who stood on stage boasting about Apple Watch&#8217;s position among all watches.</p>\\n\\n<p>Traditional watches are Apple&#8217;s competition for <em>nicest</em> watch. And Apple Watch just isn&#8217;t there. It&#8217;s not even close. Don&#8217;t get me wrong &#8212; Apple Watch <em>is</em> nice, and always been. I think that&#8217;s ultimately what defined the minimum viable product for the original Apple Watch. Apple could have made something that did what the original Apple Watch did years earlier, I&#8217;m sure. But it wouldn&#8217;t have been nice enough. But as nice as Apple Watch has always been, there are many watches that are nicer. And that makes Apple Watch unique in the history of the company. What successful product has Apple ever made that wasn&#8217;t at least arguably the nicest in its category? Apple Watch is the first.</p>\\n\\n<p>Apple Watch is a hit despite this because it&#8217;s such a great product. People love it for what it does, how it works, and for how nice it actually is. Apple Watch is thriving despite being far from the nicest watch because <em>all</em> of the watches that are nicer do so much less. That&#8217;s the flip side of Apple Watch&#8217;s anomalous status in Apple history. Apple&#8217;s products, especially new ones, generally do <em>less</em> than their competitors. Apple Watch is taking over the watch industry because it does so very, very much more than traditional watches could ever do.</p>\\n\\n<p>A thought experiment that practically proves my argument: Most of the watches that are nicer than Apple Watch only tell the time and date. Often not even the date. If Apple Watch had been exactly as we know it &#8212; same shape, same materials, same display, and the same prices &#8212; but functionally did nothing other than show the date and time, would Apple Watch be the number one watch in the world? By <em>any</em> measure? No. It would be absurd. Conversely, if Apple <em>were</em> to actually make a watch that only displayed the time and date, it wouldn&#8217;t look anything like Apple Watch as we know it. It would be so much nicer. It probably would be one of the nicest watches in the world.</p>\\n\\n<p>The luxury watch market is in large part about niceness. No one buys a Rolex or Omega or Panerai or Patek Philippe because of its timekeeping accuracy. They buy them because of how nice they are. Jony Ive is a watch guy. He knows this. Phil Schiller is a watch guy. Apple is full of people who love traditional watches, because they appreciate craftsmanship, attention to detail, typography. Nice watches are all about design down to the smallest details.</p>\\n\\n<p>Of course it bothers Apple that Apple Watch can&#8217;t do all the things that it does and fit into one of the nicest watch cases in the world. At some level it must kill them. They&#8217;re winning, but they don&#8217;t just want to win the race. They want to win the race while driving the best-looking car on the track.</p>\\n\\n<p>I&#8217;ve known this ever since I saw Apple Watch introduced in September 2014, but I was never able to put my finger precisely on <em>niceness</em> as the key to understanding Apple&#8217;s otherwise somewhat baffling approach to the product. Wearing an Apple Watch Series 4 for a few days, and taking time to consider why I&#8217;m so fond of it, prompted a moment of clarity.</p>\\n\\n<p>An appreciation of nice watches, and an honest reckoning of where Apple Watch stands in that regard, informs everything about the entire product, including, I think, the absurdly expensive 18-karat gold Edition models in the original lineup. The fundamental problem Apple faces is that the smallest possible computer they can make &#8212; today &#8212; to do what they want Apple Watch to do isn&#8217;t small enough to fit it into a watch case of size and shape that would be considered among the very <em>nicest</em> in the world.</p>\\n\\n<p>Every other aspect of Apple Watch other than the case is, in fact, world-class nice. The default watch strap, the Sport Band, is absolutely wonderful. Jony Ive&#8217;s close friend Marc Newson is <a href=\\"https://www.ablogtowatch.com/10-interesting-facts-marc-newson-watch-design-work-ikepod/\\">renowned in the watch world</a>. Ive brought Newson to Apple to make an even better version of his 1996 Ikepod strap. You know what&#8217;s not nice about most watch straps? The extra bit of strap that sticks out after you buckle it. Newson&#8217;s insight, that it could be neatly tucked <em>under</em> the other side of the strap, is simply genius. Tens of millions of Apple Watch owners now enjoy this design. And that&#8217;s just the default strap &#8212; Apple Watch&#8217;s well-liquor straps are far better-designed than the top-shelf-liquor straps from many luxury watchmakers.</p>\\n\\n<p>Apple&#8217;s higher-end bands put most Swiss watch companies to shame. Apple&#8217;s link bracelet is extremely nice, and features a way to add and remove links to adjust the size that requires nothing more than your thumbnail. No one else has a link bracelet like this. The whole idea of easily swappable bands and straps &#8212; using nothing more than your thumbnail &#8212; is an astounding innovation. It&#8217;s a key driver of Apple Watch&#8217;s success <em>as a watch</em>. People have been wearing wristwatches for over 100 years, but until Apple entered the market no company had ever thought to design a connector system that would allow for seasonal new straps and bands. It helps make Apple Watch fun for owners and helps make money for Apple.</p>\\n\\n<p>Apple didn&#8217;t start with one band and slowly grow its lineup over time. They entered on day one with an incredible strap lineup. No one would say Apple Watch debuted as the nicest watch in the world. But you can argue it debuted with the nicest lineup of straps.</p>\\n\\n<p>Apple has long been guided by a good/better/best approach to its product lines. But the stainless steel Apple Watches are <em>identical</em> functionally to the aluminum models. They cost hundreds of dollars more and the only thing that makes them better is that they&#8217;re made from nicer materials. That makes no sense at all in the world of computers. It makes perfect sense in the world of watches. I think Jony Ive made those gold Edition models and drove his team to create such a wide lineup of straps on day one to send a message. <a href=\\"https://www.hodinkee.com/articles/jony-ive-apple-watch-collector-hodinkee-magazine\\">Ive owns and admits to still occasionally wearing</a> a few traditional watches (his favorite: a stainless steel Patek Philippe Nautilus<sup id=\\"fnr1-2018-09-19\\"><a href=\\"#fn1-2018-09-19\\">1</a></sup>) and he wanted to prove that he wasn&#8217;t lowering his standards one iota, and that there&#8217;s no aspect of the watch industry &#8212; from working with precious metals to designing a perfect deployment clasp &#8212; that Apple couldn&#8217;t do at the highest level.</p>\\n\\n<hr />\\n\\n<p>The Series 4 Apple Watch is defined by being a nicer watch. The upcoming ECG feature is deservedly headline grabbing, but I wouldn&#8217;t even consider buying a Series 4 to replace my year-old Series 3 if it still looked the same. The only reason I&#8217;m even considering buying a Series 4 is that it looks and feels so much nicer.</p>\\n\\n<p>Apple has this diagram on their nifty [Apple Watch Comparison page], where the Series 4 and 3 watches are reduced to icons to convey their relative dimensions:</p>\\n\\n<p><img\\n src=\\"https://daringfireball.net/misc/2018/09/series-4-review/series4-series3-compare.png\\"\\n alt=\\"Apple\'s illustration comparing case thickness of Series 4 and Series 3.\\"\\n/></p>\\n\\n<p>That the Series 4 watch is rendered so much thinner than the Series 3 even though the stated difference in thickness is only 0.7&thinsp;mm may strike you as shameless marketing exaggeration. But after wearing and looking at a Series 4 watch on my wrist all week, I&#8217;d say this illustration conveys the difference completely accurately, and far better than any side-by-side photograph could.</p>\\n\\n<p>For watches, 0.7&thinsp;mm is significant. The Series 4 Apple Watch sits better on the wrist. It doesn&#8217;t look nearly so chubby.</p>\\n\\n<p>My review unit is a 44mm model in stainless steel with the new gold finish. It&#8217;s smaller by volume than the Series 0-3 42mm models, but larger by surface area. And the display simply seems immense. It makes me wonder if I might not prefer the new 40mm size, the display of which is slightly larger than the display of the old 42mm models. I would encourage anyone on the fence about which size to get to go to a store and try them on before deciding. It&#8217;s not that I think this 44mm model is too big for me, it&#8217;s that I wonder if the 40mm model would be big enough.</p>\\n\\n<p>Apple provided me with the gold Milanese loop as well. I wore it around the house for a day. It&#8217;s very nice, but not my style.</p>\\n\\n<p>The gold is a very interesting color. It really has quite a different effect depending on which strap you wear with it. I&#8217;ve been wearing it with a black Nike Sport band (they call the color <a href=\\"https://www.bestbuy.com/site/apple-nike-sport-band-for-apple-watch-42mm-anthracite-black/5540605.p?skuId=5540605\\">Anthracite</a>), and I&#8217;m amazed at how much I like the combination. I don&#8217;t generally like gold, but I do like this gold with a black strap.</p>\\n\\n<p>The gold finish is applied using a physical vapor deposition (PVD) process. Apple tells me this process is very similar to the process that applies the diamond like coating (DLC) to the space black watches. One thing about both of these processes is that they take several hours to apply per watch, according to Apple. That&#8217;s why the space black stainless steel models have always been more expensive. But the gold Apple Watch models cost the same as the regular stainless steel models ($699 for 40mm, $749 for 44mm). And, in a nice touch, the space black models are now the same price as regular stainless steel as well.</p>\\n\\n<p>The Series 4 Digital Crown is clearly all new. Apple &#8212; during the event and in their marketing materials &#8212; is trumpeting the Crown&#8217;s new haptic feedback. It &#8220;clicks&#8221; as you spin it, and the clicks correspond to whatever it is you&#8217;re scrolling. This is a very nice touch. But the best thing about the new Digital Crown is how freely it spins. There&#8217;s almost no friction at all. It makes the Crown on my Series 3 watch feel like it&#8217;s rusty. The feel of this new Digital Crown is so much nicer than the old ones.</p>\\n\\n<p>I&#8217;ve long believed through personal experience that haptic taps felt noticeably better on aluminum Apple Watch models than the stainless steel ones. With my Series 0 space black watch, taps were so faint I often didn&#8217;t feel them. It makes sense that it would be more difficult to provide good haptic feedback through a more rigid material. But in way it&#8217;s counterintuitive that the more expensive models would provide a worse experience for one of Apple Watch&#8217;s key features. The taps on this Series 4 watch are the best I&#8217;ve ever felt on any Apple Watch. They&#8217;re strong but not too strong. The Series 4 pages at Apple.com don&#8217;t seem to even mention the Taptic Engine, though. I asked Apple if they improved the Taptic Engine for Series 4, and the answer was something like, &#8220;We&#8217;re always working to improve every aspect of the experience&#8221; &#8212; typical Apple-ese for &#8220;We don&#8217;t want to answer that.&#8221; They <em>did</em> say though, that the Taptic Engine should feel better because the Series 4 watch sits better on the wrist. Perhaps that explains what I&#8217;m feeling, but I suspect it&#8217;s both &#8212; that taps are helped simply because the watch sits better on the wrist <em>and</em> Apple improved the Taptic Engine.</p>\\n\\n<p>Back in September 2014 at the event where Apple Watch was unveiled, I had a post-event briefing where I got to spend time examining and trying several prototype Apple Watches. (Remember: Apple announced it in September 2014, but it didn&#8217;t begin shipping until late April 2015.) <a href=\\"https://daringfireball.net/2018/09/iphone_xs_xr_series_4_apple_watch_event\\">In my post-event thoughts and observations piece</a>, I wrote:</p>\\n\\n<blockquote>\\n <p>The digital crown feels amazing. It didn’t actually control\\nanything on-screen on the demo watches I handled last week, but it\\nhas the most amazing feel of any analog controller I’ve ever used.\\n<a href=\\"https://www.google.com/search?q=define:lubricious\\">Lubricious</a> (in the second sense, if not the first as well) is the\\nword that springs to mind.</p>\\n</blockquote>\\n\\n<p>This Digital Crown feels exactly how I remember that prototype Digital Crown feeling. Lubricious. I also vividly recall that the taps I got from those prototype watches felt almost humane &#8212; as though I were being tapped on the wrist by a friend trying to subtly get my attention. That&#8217;s what the taps on this watch feel like. Assertive, but polite. In the way that a notification sound can be pleasant, these taps are pleasant. This makes me think it took Apple four years to get to the point where the Digital Crown and Taptic Engine in production Apple Watches feel the way they&#8217;ve wanted them to feel all along. In hindsight I&#8217;m rather shocked that Apple granted me hands-on time with what were clearly prototypes.</p>\\n\\n<p>Which brings us to the most striking new hardware on the Series 4: the display. I cheated a bit when I wrote the following bit in my <a href=\\"https://daringfireball.net/2018/09/iphone_xs_xr_series_4_apple_watch_event\\">thoughts and observations piece</a> regarding last week&#8217;s event, because I&#8217;d been wearing this review unit for several days already:</p>\\n\\n<blockquote>\\n <p>With the exception of the Photos watch face (which Apple added to\\nearly models only grudgingly, knowing it looked bad but also\\nknowing people would want it), previous Apple Watch faces all took\\nadvantage of the way OLED&#8217;s deep black could blend in almost\\nseamlessly with the surrounding black bezel to effectively hide\\nthe corners of the display. A sharp-cornered rectangular display\\ndoesn&#8217;t look good on a round-cornered device. The entire concept\\nwas to blur the transition from the edges of the display to the\\nbezel. The Series 4 watch faces embrace the corners of the\\ndisplay, <em>celebrate</em> the corners even, enabling fun and colorful\\nwatch faces that Apple surely never even considered for previous\\nmodels. All previous Apple Watch faces were dark; most of the new\\nones are bright and colorful. It&#8217;s a big change.</p>\\n</blockquote>\\n\\n<p>There are a few new watch faces exclusive to Series 4, including its default watch face, Infograph. Infograph Modular is also exclusive to Series 4. This isn&#8217;t marketing spite &#8212; they just wouldn&#8217;t fit on the old displays. The other new full-bleed faces &#8212; Fire and Water, Kaleidoscope, Liquid Metal, and Vapor &#8212; are available on all watches running WatchOS 5, but they look far better on Series 4. On older watches they fill a cicle in the middle of the display. On Series 4 they fill the display. I feel like it was a mistake for Apple to put any of them on the older watches. The Series 0-3 watches were meant to have faces with black backgrounds. Breathe is the only new face that I think looks at home on both old and new watches, but that&#8217;s because it isn&#8217;t meant to go full-bleed on the Series 4.</p>\\n\\n<p>These colorful new full-screen watch faces look good and look fun. They make all the previous analog faces with black backgrounds look a bit staid. Me, I like staid. But a lot of people like fun more than staid.</p>\\n\\n<p>But the other thing I&#8217;ve found is that the older watch faces, at least the analog ones, don&#8217;t look as good on a Series 4 watch as they do on Series 0-3. The old faces look better on the old watches and the new faces look better on the new ones.</p>\\n\\n<p>Here&#8217;s an example. My very favorite watch face since Series 0 in 2015 has been Utility. I prefer minimal, uncluttered faces. This is how I&#8217;ve run Utility for years:</p>\\n\\n<p><img\\n src = \\"/misc/2018/09/series-4-review/series3-utility.png\\"\\n alt = \\"Screenshot of the Utility watch face on a Series 3 Apple Watch.\\"\\n width = \\"50%\\"\\n/></p>\\n\\n<p>Here&#8217;s what that layout looks like on Series 4:</p>\\n\\n<p><img\\n src = \\"/misc/2018/09/series-4-review/series4-utility.png\\"\\n alt = \\"Screenshot of the Utility watch face on a Series 4 Apple Watch.\\"\\n width = \\"50%\\"\\n/></p>\\n\\n<p>I don&#8217;t like the temperature at an angle up there at 11 o&#8217;clock. It fits with the Series 4 aesthetic where complications follow the curve of the dial rather than sit straight up and down in the corners, but it doesn&#8217;t look right to me. Because it&#8217;s only two characters, it does look like it&#8217;s following the curve of the dial. It just looks crooked. I don&#8217;t know that it would look better the old way either. The nature of the Series 4 has changed too much with this bigger display. It sounds like <em>roll-your-eyes-prima-donna-designer</em> talk, but Apple&#8217;s faces really are designed hand-in-hand with the hardware.<sup id=\\"fnr2-2018-09-19\\">[2]</sup></p>\\n\\n<p>What I like better is this layout using the new Infograph face:</p>\\n\\n<p><img\\n src = \\"/misc/2018/09/series-4-review/series4-infograph.png\\"\\n alt = \\"Screenshot of the Utility watch face on a Series 4 Apple Watch.\\"\\n width = \\"50%\\"\\n/></p>\\n\\n<p>It&#8217;s nowhere near as minimal, but that low-high temperature graph does provide useful information at a glance. And it looks like it&#8217;s meant to follow the curve of the dial. In the abstract, just looking at them as screenshots, I like this Infograph layout the least of all three, but on the Series 4 watch, on my wrist, I like it the most.</p>\\n\\n<h2>Miscellaneous</h2>\\n\\n<ul>\\n<li><p>As promised, the speaker is much louder. It&#8217;s great for making short phone calls. The people I spoke to via calls over the watch said I sounded good, too. But I say &#8220;short calls&#8221; because it&#8217;s tiresome to hold your wrist in front of your mouth. </p></li>\\n<li><p>Infograph in its default configuration is beautiful, but in my opinion far too busy to be the default watch face. It&#8217;s the most information-dense face you can configure. And the default clock dial has a white background, which is even more distracting than the black background for Infograph that Apple is using in Series 4 product marketing photographs and video.</p></li>\\n<li><p>Even the back of the Series 4 watch looks cooler.</p></li>\\n<li><p>Complications have always been fun to play around with. It&#8217;s not full-on designing, but it is tinkering. You can lose a lot of time just tinkering around with Infograph alone.</p></li>\\n<li><p>Setting up a new Apple Watch still takes a very long time. It&#8217;s not a nice experience.</p></li>\\n<li><p>The side button now sits perfectly flush with the case, but is just as easy to press. That&#8217;s nice.</p></li>\\n<li><p>I haven&#8217;t fallen down this week.</p></li>\\n</ul>\\n\\n<h2>The Bottom Line</h2>\\n\\n<p>The Series 4 Apple Watch models cost more than the Series 3 models did last year. Last year the Series 3 models started at $329 without cellular, $399 with. This year the Series 4 starts at $399 without cellular, $499 with.</p>\\n\\n<p>That doesn&#8217;t seem right, you might think. You were waiting for these, and you love what you see, but they cost more than you expected to pay.</p>\\n\\n<p>Welcome to the world of nicer watches.</p>\\n\\n<div class=\\"footnotes\\">\\n<hr />\\n<ol>\\n<li id=\\"fn1-2018-09-19\\">\\n<p><a href=\\"https://www.patek.com/en/collection/nautilus/5711-1A-010\\">Retail: $43,000</a>. Also, do those hour and minute hands on the Nautilus look familiar?&nbsp;<a href=\\"#fnr1-2018-09-19\\" class=\\"footnoteBackLink\\" title=\\"Jump back to footnote 1 in the text.\\">&#x21A9;&#xFE0E;</a></p>\\n</li>\\n<li id=\\"fn2-2018-09-19\\">\\n<p>This is why I continue to believe Apple will never open Apple Watch to free-form third-party watch faces.&nbsp;<a href=\\"#fnr2-2018-09-19\\" class=\\"footnoteBackLink\\" title=\\"Jump back to footnote 2 in the text.\\">&#x21A9;&#xFE0E;︎</a></p>\\n</li>\\n\\n</ol>\\n</div>","permalinkUrl":"https://daringfireball.net/2018/09/apple_watch_series_4","standardLinks":{"alternate":[{"title":"★ Apple Watch Series 4","href":"https://daringfireball.net/2018/09/apple_watch_series_4","rel":"alternate","type":"text/html","language":"en"}],"shorturl":[{"title":"★ Apple Watch Series 4","href":"http://df4.us/r4t","rel":"shorturl","language":"en"}]},"actor":{"displayName":"John Gruber","permalinkUrl":"http://daringfireball.net/","id":"John Gruber","language":"en"},"source":{"id":"https://daringfireball.net/feeds/main","title":"Daring Fireball","updated":1537379005,"published":1537379005,"permalinkUrl":"https://daringfireball.net/","standardLinks":{"alternate":[{"title":"Daring Fireball","href":"https://daringfireball.net/","rel":"alternate","type":"text/html"}],"self":[{"title":"Daring Fireball","href":"https://daringfireball.net/feeds/main","rel":"self","type":"application/atom+xml"}]},"status":{"code":200,"http":"Fetched (selfPing) 200 600 and parsed 1/48 entries","nextFetch":1537379673,"lastFetch":1537379073,"lastParse":1537379073,"lastMaintenanceAt":1537364634,"period":600,"velocity":2.9,"popularity":0,"entriesCountSinceLastMaintenance":1,"feed":"https://daringfireball.net/feeds/main"}},"language":"en"}]}',
    }


def test_lambda_handler2(apigw_event2):
    ret = app.handler(apigw_event2, "")
    assert ret.get('statusCode') == 200


@pytest.fixture()
def apigw_event2():
    return {
        'pathParameters': {
            'id': '1956576f-c82a-49d3-b23e-0eb9c5dde718'
        },
        'body': '{"status": {"code": 0,"http": "Fetched (ring) 0 1200","nextFetch": 1537403266,"entriesCountSinceLastMaintenance": 1,"velocity": 2.9,"period": 1200,"lastFetch": 1537402066,"lastParse": 1537401454,"lastMaintenanceAt": 1537364634,"feed": "https://daringfireball.net/feeds/main"},"title": "","updated": null,"id": ""}',
    }


def test_lambda_handler3(apigw_event3):
    ret = app.handler(apigw_event3, "")
    assert ret.get('statusCode') == 404


@pytest.fixture()
def apigw_event3():
    return {
        'pathParameters': {
            'id': 'dc9c8333-9a89-4c4c-b8aa-b899b691aed7'
        },
        'body': '',
    }