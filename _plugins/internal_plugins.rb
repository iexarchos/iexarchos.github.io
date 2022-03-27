module Jekyll
  # {% pdf TITLE | FILE %}
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
      if input_split.size == 1
        title = file
      else
        title = context[input_split[1].strip] || input_split[1].strip
      end

      return "<iframe width=\"100%\" height=\"600px\" title=\"#{title}\" src=\"/lib/pdf.js/web/viewer.html?file=#{file}\"></iframe>"
    end
  end
end

Liquid::Template.register_tag('pdf', Jekyll::PDFTag)