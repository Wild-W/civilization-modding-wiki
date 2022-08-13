---
tags:
- RequirementType
title: REQUIREMENT_TEAM_HAS_MOST_RELIGION_FOLLOWERS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_HAS_MOST_RELIGION_FOLLOWERS
>
> * Class: `TEAMS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="VICTORY_RELIGIOUS_HAVE_MOST_FOLLOWERS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"VICTORY_RELIGIOUS_HAVE_MOST_FOLLOWERS",
		"REQUIREMENT_TEAM_HAS_MOST_RELIGION_FOLLOWERS"
	);

```
