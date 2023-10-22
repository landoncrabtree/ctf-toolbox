for i in {start..end}; do  
    result=$(openssl enc -aes-128-cbc -nosalt -d -pass pass:$i -in ciphertext -out /dev/stdout 2>/dev/null) 
    if [[ $result == *"flag"* ]]; then
        echo $result
        echo $i
        break
    fi
done

# to generate timestamps:
# from datetime import datetime, timedelta, timezone

# # timezone = gmt
# start = datetime(2023, 1, 1, tzinfo=timezone.utc)
# end = start + timedelta(days=1)

# start = int(start.timestamp())
# end = int(end.timestamp())
