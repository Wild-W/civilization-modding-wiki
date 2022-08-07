---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_BLOCK_UNIT_ENTRY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_BLOCK_UNIT_ENTRY
>
> * Class: `PLAYERS`
> * Parameters:
>	* UnitType `String`

## Samples

```SQL {title="MUSIC_CENSORSHIP_BLOCK_ROCK_BAND_ENTRY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"MUSIC_CENSORSHIP_BLOCK_ROCK_BAND_ENTRY",
		"MODIFIER_PLAYER_ADJUST_BLOCK_UNIT_ENTRY"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MUSIC_CENSORSHIP_BLOCK_ROCK_BAND_ENTRY",
		"UnitType",
		"UNIT_ROCK_BAND"
	);
	
```

