import streamlit as st
import requests
import time

def fetch_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    res = requests.get(url)

    if res.status_code != 200:
        return None

    data = res.json()

    pokemon_data = {
        "name": data["name"].title(),
        "weight": data["weight"] /100,  # Convert to kg
        "id": data["id"],
        "image": data["sprites"]["other"]["official-artwork"]["front_default"],
        "types": [t["type"]["name"].title() for t in data["types"]]
    }

    return pokemon_data


st.title("Pokémon Information")
name = st.text_input("Pokémon Name", placeholder="e.g. pikachu")


if st.button("Fetch"):
    if name.strip() == "":
        st.warning("Please enter a Pokémon name.")
    else:
        with st.spinner("Fetching Pokémon data..."):
            data = fetch_pokemon(name)

        if data:
            st.success(f"{data['name']} found!")
            col1, col2 = st.columns([1,1])

            with col1:
                st.image(data["image"], caption=f"{data['name']}", width=250)

            with col2:
                st.markdown(f"**{name}'s information is below :**")
                st.markdown('---')
                st.markdown(f"### ID:     {data['id']}")
                st.markdown(f"### Weight: {data['weight']} kg")
                st.markdown(f"### Types:  {', '.join(data['types'])}")
        else:
            st.error("Pokémon not found. Please check the name and try again.")

