# Imports
from sumy.summarizers.lex_rank import LexRankSummarizer 
#Plain text parsers since we are parsing through text
from sumy.parsers.plaintext import PlaintextParser
#for tokenization
from sumy.nlp.tokenizers import Tokenizer

# Package from: sumy 0.8.1: https://pypi.org/project/sumy/
# Github: https://github.com/miso-belica/sumy
# BBC news dataset: http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip

def run(): 
    print("Running : test_lexrank_summarizer_with_sumy")
    
    # Name of the plain-text file ~ bbc news dataset
    file = r"C:\Users\jerem\Desktop\bbc\politics\001.txt"

    # Init tools
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    

    # Summarize the document with 2 sentences
    summary = summarizer(parser.document, 2) 
    for sentence in summary:
        print(sentence)

    # Summarize from string
    string = ''' Labour plans maternity pay rise

    Maternity pay for new mothers is to rise by £1,400 as part of new proposals announced by the Trade and Industry Secretary Patricia Hewitt.

    It would mean paid leave would be increased to nine months by 2007, Ms Hewitt told GMTV's Sunday programme. Other plans include letting maternity pay be given to fathers and extending rights to parents of older children. The Tories dismissed the maternity pay plan as "desperate", while the Liberal Democrats said it was misdirected.

    Ms Hewitt said: "We have already doubled the length of maternity pay, it was 13 weeks when we were elected, we have already taken it up to 26 weeks. "We are going to extend the pay to nine months by 2007 and the aim is to get it right up to the full 12 months by the end of the next Parliament." She said new mothers were already entitled to 12 months leave, but that many women could not take it as only six of those months were paid. "We have made a firm commitment. We will definitely extend the maternity pay, from the six months where it now is to nine months, that's the extra £1,400." She said ministers would consult on other proposals that could see fathers being allowed to take some of their partner's maternity pay or leave period, or extending the rights of flexible working to carers or parents of older children. The Shadow Secretary of State for the Family, Theresa May, said: "These plans were announced by Gordon Brown in his pre-budget review in December and Tony Blair is now recycling it in his desperate bid to win back women voters."

    She said the Conservatives would announce their proposals closer to the General Election. Liberal Democrat spokeswoman for women Sandra Gidley said: "While mothers would welcome any extra maternity pay the Liberal Democrats feel this money is being misdirected." She said her party would boost maternity pay in the first six months to allow more women to stay at home in that time.

    Ms Hewitt also stressed the plans would be paid for by taxpayers, not employers. But David Frost, director general of the British Chambers of Commerce, warned that many small firms could be "crippled" by the move. "While the majority of any salary costs may be covered by the government's statutory pay, recruitment costs, advertising costs, retraining costs and the strain on the company will not be," he said. Further details of the government's plans will be outlined on Monday. New mothers are currently entitled to 90% of average earnings for the first six weeks after giving birth, followed by £102.80 a week until the baby is six months old.
    '''
    parser = PlaintextParser.from_string(string, Tokenizer("english"))
    summary = summarizer(parser.document, 2) 
    for sentence in summary:
        print(sentence)
    
    string2 = '''
        The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price.
        The deal, first reported by The Real Deal, was for $150 million, according to a source familiar with the deal.
        Mubadala, an Abu Dhabi investment fund, purchased 90% of the building for $800 million in 2008.
        Real estate firm Tishman Speyer had owned the other 10%.
        The buyer is RFR Holding, a New York real estate company.
        Officials with Tishman and RFR did not immediately respond to a request for comments.
        It's unclear when the deal will close.
        The building sold fairly quickly after being publicly placed on the market only two months ago.
        The sale was handled by CBRE Group.
        The incentive to sell the building at such a huge loss was due to the soaring rent the owners pay to Cooper Union, a New York college, for the land under the building.
        The rent is rising from $7.75 million last year to $32.5 million this year to $41 million in 2028.
        Meantime, rents in the building itself are not rising nearly that fast.
        While the building is an iconic landmark in the New York skyline, it is competing against newer office towers with large floor-to-ceiling windows and all the modern amenities.
        Still the building is among the best known in the city, even to people who have never been to New York.
        It is famous for its triangle-shaped, vaulted windows worked into the stylized crown, along with its distinctive eagle gargoyles near the top.
        It has been featured prominently in many films, including Men in Black 3, Spider-Man, Armageddon, Two Weeks Notice and Independence Day.
        The previous sale took place just before the 2008 financial meltdown led to a plunge in real estate prices.
        Still there have been a number of high profile skyscrapers purchased for top dollar in recent years, including the Waldorf Astoria hotel, which Chinese firm Anbang Insurance purchased in 2016 for nearly $2 billion, and the Willis Tower in Chicago, which was formerly known as Sears Tower, once the world's tallest.
        Blackstone Group (BX) bought it for $1.3 billion 2015.
        The Chrysler Building was the headquarters of the American automaker until 1953, but it was named for and owned by Chrysler chief Walter Chrysler, not the company itself.
        Walter Chrysler had set out to build the tallest building in the world, a competition at that time with another Manhattan skyscraper under construction at 40 Wall Street at the south end of Manhattan. 
        He kept secret the plans for the spire that would grace the top of the building, building it inside the structure and out of view of the public until 40 Wall Street was complete.
        Once the competitor could rise no higher, the spire of the Chrysler building was raised into view, giving it the title.
    '''
    parser = PlaintextParser.from_string(string2, Tokenizer("english"))
    summary = summarizer(parser.document, 2) 
    for sentence in summary:
        print(sentence)