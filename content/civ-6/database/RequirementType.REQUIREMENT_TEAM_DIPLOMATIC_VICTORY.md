---
tags:
- RequirementType
title: REQUIREMENT_TEAM_DIPLOMATIC_VICTORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_DIPLOMATIC_VICTORY
>
> * Class: `TEAMS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="DIPLOMATIC_VICTORY_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"DIPLOMATIC_VICTORY_REQUIREMENT",
		"REQUIREMENT_TEAM_DIPLOMATIC_VICTORY"
	);

```
