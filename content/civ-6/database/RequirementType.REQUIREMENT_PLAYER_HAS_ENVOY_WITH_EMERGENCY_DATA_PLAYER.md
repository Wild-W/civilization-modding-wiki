---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_ENVOY_WITH_EMERGENCY_DATA_PLAYER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_ENVOY_WITH_EMERGENCY_DATA_PLAYER
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_ENVOYS_AT_EMERGENCY_CITY_STATE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_ENVOYS_AT_EMERGENCY_CITY_STATE",
		"REQUIREMENT_PLAYER_HAS_ENVOY_WITH_EMERGENCY_DATA_PLAYER"
	);


```
