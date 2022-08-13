---
tags:
- RequirementType
title: REQUIREMENT_DEMAND_RECEIVED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_DEMAND_RECEIVED
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLAYER_RECEIVED_DEMAND"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_RECEIVED_DEMAND",
		"REQUIREMENT_DEMAND_RECEIVED",
		1
	);

```
