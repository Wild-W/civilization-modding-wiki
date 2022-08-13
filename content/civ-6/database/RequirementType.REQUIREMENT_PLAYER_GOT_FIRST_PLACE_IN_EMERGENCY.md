---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_GOT_FIRST_PLACE_IN_EMERGENCY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_GOT_FIRST_PLACE_IN_EMERGENCY
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_IN_FIRST_PLACE_FOR_EMERGENCY_SCORE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_IN_FIRST_PLACE_FOR_EMERGENCY_SCORE",
		"REQUIREMENT_PLAYER_GOT_FIRST_PLACE_IN_EMERGENCY"
	);

```
