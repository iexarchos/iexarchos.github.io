module Jekyll
  # {% pdf FILE | TITLE | PATHPREFIX %}
  # creates an iframe with title `TITLE` for displaying a PDF located at `FILE`
  # uses PDF.js for rendering PDFs
  class PDFTag < Liquid::Tag
    def initialize(tag_name, input, tokens)
      super
      @input = input
    end
  
    def render(context)
      input_split = @input.split("|")
      file = context[input_split[0].strip] || input_split[0].strip
      pathprefix = ""
      if input_split.size == 1
        title = file
      elsif input_split.size == 2
        title = context[input_split[1].strip] || input_split[1].strip
      else
       title = context[input_split[1].strip] || input_split[1].strip
       pathprefix = context[input_split[2].strip] || input_split[2].strip
      end
      return "<iframe width=\"100%\" height=\"600px\" title=\"#{title}\" src=\"#{pathprefix}lib/pdf.js/web/viewer.html?file=#{pathprefix}#{file}\"></iframe>"
    end
  end
end

Liquid::Template.register_tag('pdf', Jekyll::PDFTag)

