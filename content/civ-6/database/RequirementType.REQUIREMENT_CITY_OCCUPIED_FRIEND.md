---
tags:
- RequirementType
title: REQUIREMENT_CITY_OCCUPIED_FRIEND
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_OCCUPIED_FRIEND
>
> * Class: `CITIES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_CITY_OCCUPIED_FRIEND"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_CITY_OCCUPIED_FRIEND",
		"REQUIREMENT_CITY_OCCUPIED_FRIEND"
	);


```
