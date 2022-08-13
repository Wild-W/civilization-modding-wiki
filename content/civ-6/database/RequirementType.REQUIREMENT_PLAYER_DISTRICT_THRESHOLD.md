---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_DISTRICT_THRESHOLD
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_DISTRICT_THRESHOLD
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinDistrictsNeeded `Integer`
>	* DistrictPercentThreshold `Integer`
>	* AboveThreshold `Boolean`

## Samples

```SQL {title="REQUIRES_LAGS_DISTRICTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_LAGS_DISTRICTS",
		"REQUIREMENT_PLAYER_DISTRICT_THRESHOLD"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_LAGS_DISTRICTS",
		"AboveThreshold",
		0
	),
	(
		"REQUIRES_LAGS_DISTRICTS",
		"DistrictPercentThreshold",
		60
	),
	(
		"REQUIRES_LAGS_DISTRICTS",
		"MinDistrictsNeeded",
		3
	);
	
```
