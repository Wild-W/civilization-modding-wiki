---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_TURN_STARTED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_TURN_STARTED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_TURN_STARTED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_TURN_STARTED",
		"REQUIREMENT_PLAYER_TURN_STARTED",
		1
	);

```
