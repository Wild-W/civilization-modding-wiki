---
tags:
- RequirementType
title: REQUIREMENT_DEFENSIVE_PACT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_DEFENSIVE_PACT
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_DEFENSIVE_PACT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_DEFENSIVE_PACT",
		"REQUIREMENT_DEFENSIVE_PACT"
	);


```
