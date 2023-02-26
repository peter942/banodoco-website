import streamlit as st


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
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)

st.sidebar.image("https://banodoco.s3.amazonaws.com/input_images/Do+(1).png",use_column_width='always')
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
    st.markdown("[Join Discord](https://discord.gg/kkjkeEaVpZ)   |   [Apply To Test](https://form.typeform.com/to/vR2VNXJV)")
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

  st.subheader("AI native tools for crafting and refining your creation")
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

    if st.session_state['feature'] == 'pipelines':
      feature_image = "https://banodoco.s3.amazonaws.com/input_images/Untitled+design+-+2023-02-26T150703.582.png"
      feature_text = "Use & build custom pipelines combining multiple models to achieve the exact effect you want"
    elif st.session_state['feature'] == 'timing':
      feature_image = "https://i.ibb.co/GHxJkd4/Untitled-design-2023-02-23-T220706-388.png"
      feature_text = "Adjust and tweak the timing to achieve your desired effect"
    elif st.session_state['feature'] == 'frame':
      feature_image = "https://i.ibb.co/0QNyK7K/Untitled-design-2023-02-23-T221038-734.png"
      feature_text = "Edit individual key frames with a variety of models until they're perfect"
    elif st.session_state['feature'] == 'backdrop':
      feature_image = "https://banodoco.s3.amazonaws.com/input_images/Untitled+design+-+2023-02-26T151015.293.png"
      feature_text = "Transform the backdrop of your video with a variety of models"
    
  
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
  st.markdown("We're looking for high-agency, talented individuals who want to take ownership over various components of the project. Below are what we're looking for right now..")
  with st.expander("Optimise existing models to make them practical for usage (ML Engineer)"):
    st.write("There are a lot of useful models out there that are either too slow or have other barriers to be usable by Banodoco. We're looking for someone to help us optimise these models to make them practical for usage.")
    st.markdown("Are you interested? Just send an email to me [here](mailto:peter@omalley.io?subject=Help%20optimising%20Banodoco%20models%20(%23BanodocoML)&body=Hi%2C%20my%20name%20is%0D%0A%0D%0ASomething%20I've%20done%20before...%0D%0A%0D%0AI'm%20interested%20because...%0D%0A%0D%0ATag%3A%20BanodocoMLOptimiser) and I'll get back if it seems like a good fit")
  with st.expander("Build out front-end components to improve editing process (JavaScript/Front-End)"):
    st.write("We're looking for someone to help us build out front-end components to improve the editing process. This could include things like a better way to select keyframes, or a better way to pan the camera.")
    st.markdown("Are you interested? Just send an email to me [here](mailto:peter@omalley.io?subject=mailto:peter@omalley.io?subject=Help%20with%20Banodoco%20Front-End%20&body=Hi%2C%20my%20name%20is%0D%0A%0D%0ASomething%20I've%20done%20before...%0D%0A%0D%0AI'm%20interested%20because...%0D%0A%0D%0ATag%3A%20BanodocoFrontEnd) and I'll get back if it seems like a good fit")
  with st.expander("Build a small model for automated key frame selection (ML)"):
    st.write("We're looking for someone to help us build a small model for automated key frame selection. This could be as simple as a model that takes in a video and outputs a list of key frames. Figuring out how to get the data do this will be a big part of the project :)")
    st.markdown("Are you interested? Just send an email to me [here](mailto:peter@omalley.io?subject=mailto:peter@omalley.io?subject=mailto:peter@omalley.io?subject=Help%20with%20Banodoco%20ML&body=Hi%2C%20my%20name%20is%0D%0A%0D%0ASomething%20I've%20done%20before...%0D%0A%0D%0AI'm%20interested%20because...%0D%0A%0D%0ATag%3A%20BanodocoML) and I'll get back if it seems like a good fit")
  with st.expander("Build out automated scenery/backdrop panning tool (Python)"):
    st.write("We're looking for someone to help us build out an automated scenery/backdrop panning tool. This will initially start as a tool that takes user input and generates backdrops based on user input (prompts or images) but should be built to evolve into an automated tool. I have a bunch of ideas on how to do this.")
    st.markdown("Are you interested? Just send an email to me [here](mailto:peter@omalley.io?subject=Help%20with%20Banodoco%20Backdrop%20Python%20project&body=Hi%2C%20my%20name%20is%0D%0A%0D%0ASomething%20I've%20done%20before...%0D%0A%0D%0AI'm%20interested%20because...%0D%0A%0D%0ATag%3A%20BanodocoPythonProject) and I'll get back if it seems like a good fit")
  with st.expander("Refine and optimise structure and speed of app (Python)"):
    st.write("I'm a software development noob and I'm sure there are a lot of ways to improve the structure and speed of the app. I'm looking for someone to help me with this.")
    st.markdown("Are you interested? Just send an email to me [here](mailto:peter@omalley.io?subject=Help%20with%20Banodoco%20Backdrop%20Optimisation%20project&body=Hi%2C%20my%20name%20is%0D%0A%0D%0ASomething%20I've%20done%20before...%0D%0A%0D%0AI'm%20interested%20because...%0D%0A%0D%0ATag%3A%20BanodocoPythonOptimiser) and I'll get back if it seems like a good fit")
  with st.expander("Other stuff you think of (???"):
    st.write("Maybe you can think of something else that would be useful to the project. If so, let me know!")
    st.markdown("Are you interested? Just send an email to me [here](mailto:peter@omalley.io?subject=Help%20with%20%3F%3F%3F&body=Hi%2C%20my%20name%20is%0D%0A%0D%0ASomething%20I've%20done%20before...%0D%0A%0D%0AI'm%20interested%20because...%0D%0A%0D%0ATag%3A%20BanodocoQuestionMark) and I'll get back if it seems like a good fit")


elif st.session_state['page'] == 'gallery':
  
  st.title("Gallery")

  


  gallery1, gallery2 = st.columns([1, 1])

  with gallery1:
    st.markdown("#### The sound of the tires in the snow #2")
    st.write("Produced: Febuary 2023")
    st.video("https://youtu.be/vWWBiDjwKkg")
    st.info("Made with: Banodoco v 0.2")
    st.markdown("***")

  with gallery2:
    st.markdown("#### The sound of the tires in the snow #1")
    st.write("Produced: Decemeber 2022")
    st.video("https://youtu.be/X_BLuno7C84")
    st.info("Made with: Banodoco v 0.1")
    st.markdown("***")

    
    
