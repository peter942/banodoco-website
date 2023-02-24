import streamlit as st
import base64


if 'page' not in st.session_state:
  st.session_state['page'] = 'home'
if 'feature' not in st.session_state:
  st.session_state['feature'] = 'timing'


main_pages = ["home", "philosophy & roadmap", "collaborate", "gallery"]

st.set_page_config(page_title="Banodoco")

hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
html, body {
    max-width: 100%;
    overflow-x: hidden;
}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

st.sidebar.image("https://i.ibb.co/xXsd2Cb/Do.png",use_column_width='always')
st.sidebar.markdown("***")
st.sidebar.write("")

for page in main_pages:        
  if page == st.session_state['page']:
    if st.sidebar.button(page.title(),type="primary"):
      st.session_state['page'] = page
      st.experimental_rerun()
  else:
    if st.sidebar.button(page.title(),type="secondary"):
      st.session_state['page'] = page
      st.experimental_rerun()

st.sidebar.markdown("***")
st.sidebar.write("")    

st.sidebar.markdown("[Join Discord](https://discord.gg/kkjkeEaVpZ)   |   [Apply To Test](https://form.typeform.com/to/vR2VNXJV)")      
st.sidebar.markdown("*Public release: March 2023*")


if st.session_state['page'] == 'home':

  header1, header2 = st.columns(2)
  with header1:
    st.header("An open-source tool for creating beautiful videos with AI")
    st.write("Banodoco is a free, open-source animation tool that aims to allow anyone to use AI to create beautiful videos of anything they can imagine.")
    st.write("It's designed for those who want precision - with an approach and tools designed to give artists enough control over various AI models to create exactly what's in their imagination.")
  with header2:
    st.image("https://i.ibb.co/6wsn9j6/Untitled-design-2023-02-24-T160623-805.png",use_column_width='always')

  st.markdown("***")

  st.subheader("Coherent and beautiful video to video transformations")
  st.write("We believe that the best way for a human to tell AI what video they want to create is with a video of their own that it transforms. Banodoco allows users to control and direct AI with pipelines that combine multiple models to achieve coherent transformations of characters, scenes, and styles.")
  comparison1, comparison2 = st.columns(2)
  with comparison1:
    st.image("https://banodoco.s3.amazonaws.com/input_images/input.gif", caption="Before",use_column_width='always')
  with comparison2:
    st.image("https://banodoco.s3.amazonaws.com/input_images/output.gif", caption="After",use_column_width='always')         
  st.info("Video prompts > word prompts. An image is worth a thousand words and a video contains 30 images per second!")

  st.markdown("***")

  st.subheader("An AI native tool for crafting and refining your creation")
  st.write("Banodoco is designed to be an AI native tool - with all of our features leveraged by AI to make your life easier. We aim to provide you with the tools to create beautiful videos with the least amount of effort possible.")
  feature1, feature2, feature3 = st.columns([1,3,1])
  with feature1:  
    if st.button("Timing Adjustment"):
      st.session_state['feature'] = 'timing'   
      st.experimental_rerun()
    if st.button("Key Frame Editing"):
      st.session_state['feature'] = 'frame'      
      st.experimental_rerun()
    if st.button("Scene transformation"):
      st.session_state['feature'] = 'backdrop'      
      st.experimental_rerun()
    if st.button("Custom Pipelines"):
      st.session_state['feature'] = 'pipelines'      
      st.experimental_rerun()
    st.markdown("*And much more...*")

    if st.session_state['feature'] == 'timing':
      feature_image = "https://i.ibb.co/GHxJkd4/Untitled-design-2023-02-23-T220706-388.png"
      feature_text = "Adjust and tweak the timing to achieve your desired effect"
    elif st.session_state['feature'] == 'frame':
      feature_image = "https://i.ibb.co/0QNyK7K/Untitled-design-2023-02-23-T221038-734.png"
      feature_text = "Edit individual key frames with a variety of models until they're perfect"
    elif st.session_state['feature'] == 'backdrop':
      feature_image = "https://i.ibb.co/0QNyK7K/Untitled-design-2023-02-23-T221038-734.png"
      feature_text = "Transform the backdrop of your video with a variety of models"
    elif st.session_state['feature'] == 'pipelines':
      feature_image = "https://i.ibb.co/0QNyK7K/Untitled-design-2023-02-23-T221038-734.png"
      feature_text = "Create your own custom pipelines to achieve the exact effect you want"
  
  with feature2:
    st.image(feature_image,use_column_width='always')
  with feature3:
    st.info(feature_text)
    
  st.markdown("***")

  a1, a2 = st.columns([1, 1])
  with a1:
    st.subheader("Become a core contributor")
    st.write("We're looking for high-agency, talented individuals who want to contribute to the project.")
    if st.button("Learn about what we're looking for"):
      st.session_state['page'] = 'collaborate'
      st.experimental_rerun()
  with a2:
    st.image("https://media.discordapp.net/attachments/1017188259102724146/1078456600781652069/peteromallet_minimalistic_illustration_of_people_building_scaff_a97eb34a-7ab1-4cae-a02e-b229ff5bcb66.png", use_column_width='always')
 
  b1, b2 = st.columns([1, 1])
  with b1:
    st.subheader("Philosophy & roadmap")
    st.write("We're building an open-source tool that will enable people to make whatever they can imagine!")
    if st.button("See our philosophy & roadmap"):
      st.session_state['page'] = 'philosophy & roadmap'
      st.experimental_rerun()
  with b2:
    st.image("https://media.discordapp.net/attachments/1017188259102724146/1078451803718438942/peteromallet_minimalistic_illustration_meaning_a_long_journey_R_5dd02f2f-1583-4f39-8eae-6348ac68062a.png", use_column_width='always')

  c1, c2 = st.columns([1, 1])
  with c1:
    st.subheader("Visit our gallery")
    st.write("While it's a little bit sparse now, we'll share the best creations made by artists using Banodoco.")
    if st.button("Visit Gallery"):
      st.session_state['page'] = 'gallery'
      st.experimental_rerun()
  with c2:
    st.image("https://media.discordapp.net/attachments/1017188259102724146/1078456680829960232/peteromallet_minimalistic_illustration_of_people_at_a_gallery_l_0992827a-34bf-4de1-b83d-52cc59c67d50.png", use_column_width='always')
  
  st.markdown("***")

  st.subheader("Join our Discord to learn about our releases, get early access to our beta, and to collaborate with other artists")
  st.write("Join our Discord to get the latest updates and to collaborate with other artists")
  st.markdown("[Join Discord](https://discord.gg/kkjkeEaVpZ)   |   [Apply To Test](https://form.typeform.com/to/vR2VNXJV)")


elif st.session_state['page'] == "philosophy & roadmap":

  header1, header2 = st.columns([1, 1])
  with header1:  
    st.subheader("A open-source tool to assist those who want to create beautiful things")
    st.write("Banodoco is named after the 4 painters who assisted Michelangelo in the creation of the Sistine Chapel. We believe that AI can provide everyone in the world with expert assistance to make their masterpieces come to life.")
  with header2:
    st.image("https://i.ibb.co/bJmHHXj/Untitled-design-2023-02-24-T013745-519.png", use_column_width='always')
  
  st.subheader("Our Principles")
  st.markdown("**For the creation of beautiful things**")
  st.write("In a world where everyone can easily create beautiful things, everything will become increasingly beautiful - so we’re focused on helping people create things that are")
  st.markdown("**For people who want control**")
  st.write("Some tools create beautiful things - but the people who use them have limited control. We want humans to be in the driver’s seat.")
  st.markdown("**Lean on humans where AI falls short**")
  st.write("We believe that AI can assist humans in creating beautiful things, but that humans will always be needed to make the final decisions.")
  st.markdown("**Work to automate the mundane**")
  st.write("We want to automate the mundane tasks that are required to create beautiful things, so that humans can focus on the creative tasks.")
  st.markdown("**Be structurally model agonistic**")
  st.write("We’ll use whatever models deliver the best results and build our tool in a way that makes it easy for others to add their own models.")
  st.markdown("**Open to our core**")
  st.write("Everything we do will be open for anyone to use for free (minus GPU costs) or for anyone to build on top of.")
  st.markdown("**Hosted to ease access**")
  st.write("While anyone can use the free version, we’ll have a hosted version available at cost of compute + 10-30%. Any profits from this will be distributed to collaborators based on a pre-defined system.")

  st.write()
  

elif st.session_state['page'] == 'collaborate':

  st.title("Contribute")
  st.write("In addition to public contributors wants we release, we'd want to deeply collaborate with brilliant people, who believe in our mission, and believe in the power of open source.")
  st.write("Everything you build will not only be open source as part of Banodoco, but will ideally but delivered in a modular way for others to easily use. For example, this means that any models created or optimised will be hosted on Replicate.com for others to easily leverage, while front-end components developed will be built as Streamlit components for others to implement.")  
  
  st.subheader("What we're looking for")
  st.write("We're looking for high-agency, talented individuals who want to contribute to the project.")
  with st.expander("Optimise existing models to make them practical for usage (ML Engineer)"):
    st.write("test")
  with st.expander("Build out front-end components to improve editing process (JavaScript/Front-End)"):
    st.write("test")
  with st.expander("Build a small model for automated key frame selection (ML)"):
    st.write("test")
  with st.expander("Build out automated backdrop positioning tool (Python)"):
    st.write("test")
  with st.expander("Refine and optimise structure and speed of app (Python)"):
    st.write("test")    
  with st.expander("Other stuff you think of (???"):
    st.write("test")  

  st.subheader("FAQ:")
  st.write("Below are some frequently asked questions - well, no one actually has asked me any quesions yet, but I guess I'll just answer them anyway.")
  with st.expander("How will it work?"):
    st.write("We'll work together to define a roadmap for the project, and then you'll be able to work on whatever you'd like, with the support of the rest of the team. We'll also be able to provide you with a stipend to support your work.")
  with st.expander("What kinds of projects?"):
    st.write("We're looking for people to work on a variety of projects, including but not limited to: optimising existing models, building new models, building out the front-end, building out the back-end, and designing the user experience.")
  with st.expander("Will I be compensatd?"):
    st.write("We'll be able to provide you with a stipend to support your work.")
  with st.expander("How much time will I need to commit?"):
    st.write("We'll work together to define a roadmap for the project, and then you'll be able to work on whatever you'd like, with the support of the rest of the team.")
  with st.expander("Who will I be working with?"):
    st.write("We'll use Discord to communicate and share updates.")
  with st.expander("How will we communicate?"):
    st.write("We'll use Discord to communicate and share updates.")


elif st.session_state['page'] == 'gallery':
  
  st.title("Gallery")
    
    
