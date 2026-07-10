import pandas as pd

def remove_names():
    df = pd.read_csv('data.csv', encoding='utf-8')
    
    col = 'sender_name'
    
    df[col] = df[col].astype(str).str.split('،', n=1).str[1].str.strip()
    
    df.to_csv('data_raw.csv', index=False, encoding='utf-8')
    

def fix_numbers():
    # Load the CSV
    df = pd.read_csv("data.csv")

    # Reset the ID column to start from 1
    df["id"] = range(1, len(df) + 1)

    # Save back to CSV
    df.to_csv("data.csv", index=False)

    print(f"Done! ID column reset for {len(df)} rows.")


if __name__ == '__main__':
    fix_numbers()