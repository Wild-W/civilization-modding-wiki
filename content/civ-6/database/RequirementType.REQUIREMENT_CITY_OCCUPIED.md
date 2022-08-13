---
tags:
- RequirementType
title: REQUIREMENT_CITY_OCCUPIED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_OCCUPIED
>
> * Class: `CITIES`
> * Arguments:
>	* OnlyOwnersCity `Boolean`

## Samples

```SQL {title="REQUIRES_PLAYER_CITY_OCCUPIED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_CITY_OCCUPIED",
		"REQUIREMENT_CITY_OCCUPIED"
	);


```

```SQL {title="CITY_IS_OCCUPIED_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"CITY_IS_OCCUPIED_REQUIREMENT",
		"REQUIREMENT_CITY_OCCUPIED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"CITY_IS_OCCUPIED_REQUIREMENT",
		"OnlyOwnersCity",
		0
	);
	
```
