from corva import Api, Cache, Logger, StreamTimeEvent, stream

@stream
def lambda_handler(event: StreamTimeEvent, api: Api, cache: Cache):
    """ Test app """
    Logger.info(f'{event=}')
    asset_id = event.asset_id
    company_id = event.company_id
    records = event.records     # fetch all records from the event

    print(records)
    Logger.info(f'Start')

    data = records[0].data      # get the data from the first record
    hook_load = data['hook_load']   # get hook_load from data
    weight_on_bit = data['weight_on_bit']   # get weight_on_bit from data
    hook_load_plus_wob = hook_load + weight_on_bit  # calculate the sum

    # compose data for our collection
    body = {
        "asset_id": asset_id,
        "version": 1,
        "timestamp": records[0].timestamp,
        "company_id": company_id,
        "data": {
            "hook_load_plus_wob": hook_load_plus_wob
        }
    }
    Logger.info(f'{body=}')
    api.post('/api/v1/data/big-data-energy/hook_load_plus_wob/', data=[body]).raise_for_status()
    Logger.info('Done!')
