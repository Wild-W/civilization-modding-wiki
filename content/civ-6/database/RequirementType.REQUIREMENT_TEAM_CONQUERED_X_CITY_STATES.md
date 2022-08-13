---
tags:
- RequirementType
title: REQUIREMENT_TEAM_CONQUERED_X_CITY_STATES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_CONQUERED_X_CITY_STATES
>
> * Class: `TEAMS`
> * Arguments:
>	* CityStatesConquered `Unknown`

## Samples

```SQL {title="PROXYWAR_VICTORY_CAPTURE_CITY_STATES"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PROXYWAR_VICTORY_CAPTURE_CITY_STATES",
		"REQUIREMENT_TEAM_CONQUERED_X_CITY_STATES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PROXYWAR_VICTORY_CAPTURE_CITY_STATES",
		"CityStatesConquered",
		3
	);
	
```
